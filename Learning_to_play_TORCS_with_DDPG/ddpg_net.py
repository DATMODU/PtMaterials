from config import *
import tensorflow as tf

class DDPG_NET(object) :

    def __init__(self):
        self.X = tf.placeholder(dtype=tf.float32, shape=[None, NUM_ASSET, WINDOW_SIZE, INPUT_FEATURES], name='X')
        self.X_ = tf.placeholder(dtype=tf.float32, shape=[None, NUM_ASSET, WINDOW_SIZE, INPUT_FEATURES], name='X_')
        self.PVM = tf.placeholder(dtype=tf.float32, shape=[None, NUM_ASSET, 1, WEIGHT_LAYER], name='PVM')
        self.PVM_ = tf.placeholder(dtype=tf.float32, shape=[None, NUM_ASSET, 1, WEIGHT_LAYER], name='PVM_')
        self.CASH_BIAS = tf.placeholder(dtype= tf.float32, shape = [None,1,1,1], name='CASH_BIAS')
        self.REWARD = tf.placeholder(dtype=tf.float32, shape=[None, 1], name='REWARD')

        with tf.variable_scope('Actor') :
            self.a = self.build_actor_net(s = self.X, pvm= self.PVM, scope = 'eval', trainable=True)
            a_ = self.build_actor_net(s = self.X_, pvm= self.PVM_, scope = 'target', trainable=False)

        with tf.variable_scope('Critic'):
            q = self.build_critic_net(s=self.X, pvm = self.PVM, a=self.a, scope='eval', trainable=True)
            q_ = self.build_critic_net(s=self.X_, pvm = self.PVM_, a=a_, scope='target', trainable=False)

        # networks parameters
        self.ae_params = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES, scope='Actor/eval')
        self.at_params = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES, scope='Actor/target')
        self.ce_params = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES, scope='Critic/eval')
        self.ct_params = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES, scope='Critic/target')

        # target net replacement
        self.soft_replace = [[tf.assign(ta, (1 - TAU) * ta + TAU * ea), tf.assign(tc, (1 - TAU) * tc + TAU * ec)]
                             for ta, ea, tc, ec in zip(self.at_params, self.ae_params, self.ct_params, self.ce_params)]

        q_target = self.REWARD + q_

        # in the feed_dic for the td_error, the self.a should change to actions in memory
        td_error = tf.losses.mean_squared_error(labels=q_target, predictions=q)

        self.ctrain = tf.train.AdamOptimizer(LEARNING_RATE).minimize(td_error, var_list=self.ce_params)

        a_loss = - tf.reduce_mean(q)    # maximize the q
        self.atrain = tf.train.AdamOptimizer(LEARNING_RATE).minimize(a_loss, var_list=self.ae_params)


        tf.summary.scalar('q', tf.reduce_mean(q))
        tf.summary.scalar('q_target', tf.reduce_mean(q_target))
        tf.summary.scalar('td_error', tf.reduce_mean(td_error))
        tf.summary.scalar('reward', tf.reduce_mean(self.REWARD))
        tf.summary.histogram('action', self.a)

        self.merged = tf.summary.merge_all()





    def build_actor_net(self, s, pvm, scope, trainable):

        with tf.variable_scope(scope):

            f1 = tf.layers.conv2d(inputs = s, filters = 2, kernel_size= [1, 3], strides=[1,1], padding = 'valid',
                                activation= tf.nn.relu,
                                kernel_initializer=tf.contrib.layers.xavier_initializer_conv2d(uniform = False),
                                kernel_regularizer=tf.contrib.layers.l2_regularizer(scale = REGULIZE_COEFF),
                                  bias_regularizer=tf.contrib.layers.l2_regularizer(scale = REGULIZE_COEFF),
                                  activity_regularizer=tf.contrib.layers.l2_regularizer(scale = REGULIZE_COEFF),
                                  trainable=trainable)

            f2 = tf.layers.conv2d(inputs = f1, filters = 1, kernel_size= [1, WINDOW_SIZE -2], strides=[1,1], padding = 'valid',
                                activation= tf.nn.relu,
                                kernel_initializer=tf.contrib.layers.xavier_initializer_conv2d(uniform = False),
                                kernel_regularizer=tf.contrib.layers.l2_regularizer(scale = REGULIZE_COEFF),
                                  bias_regularizer=tf.contrib.layers.l2_regularizer(scale = REGULIZE_COEFF),
                                  activity_regularizer=tf.contrib.layers.l2_regularizer(scale = REGULIZE_COEFF),
                                  trainable=trainable)

            f2_join = tf.concat([f2, pvm], axis = 3)

            f3 = tf.layers.conv2d(inputs = f2_join, filters = 1, kernel_size= [1, 1], strides=[1,1], padding = 'valid',
                                activation= tf.nn.relu,
                                kernel_initializer=tf.contrib.layers.xavier_initializer_conv2d(uniform = False),
                                kernel_regularizer=tf.contrib.layers.l2_regularizer(scale = REGULIZE_COEFF),
                                  bias_regularizer=tf.contrib.layers.l2_regularizer(scale = REGULIZE_COEFF),
                                  activity_regularizer=tf.contrib.layers.l2_regularizer(scale = REGULIZE_COEFF),
                                  trainable=trainable)

            f3_join = tf.concat([self.CASH_BIAS, f3], axis = 1)

            f3_reshape = tf.reshape(f3_join, [-1, NUM_ASSET + 1])

            a = tf.nn.softmax(logits=f3_reshape, dim = -1, name ='SOFT_MAX')

            return a

    def build_critic_net(self, s, pvm, a, scope, trainable):

        with tf.variable_scope(scope):

            f1 = tf.layers.conv2d(inputs = s, filters = 2, kernel_size= [1, 3], strides=[1,1], padding = 'valid',
                                activation= tf.nn.relu,
                                kernel_initializer=tf.contrib.layers.xavier_initializer_conv2d(uniform = False),
                                kernel_regularizer=tf.contrib.layers.l2_regularizer(scale = REGULIZE_COEFF),
                                  bias_regularizer=tf.contrib.layers.l2_regularizer(scale = REGULIZE_COEFF),
                                  activity_regularizer=tf.contrib.layers.l2_regularizer(scale = REGULIZE_COEFF),
                                  trainable=trainable)

            f2 = tf.layers.conv2d(inputs = f1, filters = 1, kernel_size= [1, WINDOW_SIZE -2], strides=[1,1], padding = 'valid',
                                activation= tf.nn.relu,
                                kernel_initializer=tf.contrib.layers.xavier_initializer_conv2d(uniform = False),
                                kernel_regularizer=tf.contrib.layers.l2_regularizer(scale = REGULIZE_COEFF),
                                  bias_regularizer=tf.contrib.layers.l2_regularizer(scale = REGULIZE_COEFF),
                                  activity_regularizer=tf.contrib.layers.l2_regularizer(scale = REGULIZE_COEFF),
                                  trainable=trainable)

            f2_join = tf.concat([f2, pvm], axis = 3)

            f3 = tf.layers.conv2d(inputs = f2_join, filters = 1, kernel_size= [1, 1], strides=[1,1], padding = 'valid',
                                activation= tf.nn.relu,
                                kernel_initializer=tf.contrib.layers.xavier_initializer_conv2d(uniform = False),
                                kernel_regularizer=tf.contrib.layers.l2_regularizer(scale = REGULIZE_COEFF),
                                  bias_regularizer=tf.contrib.layers.l2_regularizer(scale = REGULIZE_COEFF),
                                  activity_regularizer=tf.contrib.layers.l2_regularizer(scale = REGULIZE_COEFF),
                                  trainable=trainable)
            
            f3_join = tf.concat([self.CASH_BIAS, f3], axis=1)

            f3_reshape = tf.reshape(f3_join, [-1, NUM_ASSET + 1])

            w1_s = tf.get_variable('w1_s', [NUM_ASSET + 1, N_CRITIC], trainable=trainable)
            w1_a = tf.get_variable('w1_a', [NUM_ASSET + 1, N_CRITIC], trainable=trainable)
            b1 = tf.get_variable('b1', [1, N_CRITIC], trainable=trainable)

            net = tf.nn.relu(tf.matmul(f3_reshape, w1_s) + tf.matmul(a, w1_a) + b1)

            q = tf.layers.dense(net, 1, trainable = trainable)

            return q



    def choose_action(self, session, state, pvm, cash_bias):
        """
        :param session: get tf session
        :param state: price tensor X
        :param pvm: portfoilo vector memory
        :return: action from poliy network
        """
        a = session.run(self.a, feed_dict = {self.X : state, self.PVM : pvm, self.CASH_BIAS : [[[[cash_bias]]]]})


        return a[0]



    def init_optimizer(self):

        self.parameters_gradients = tf.gradients(self.action, self.pg_params, self.REWARD)
        opt = tf.train.AdamOptimizer(learning_rate= -1*LEARNING_RATE)
        self.train_op = opt.apply_gradients(zip(self.parameters_gradients, self.pg_params))
        #self.train_op = opt.minimize(loss = self.REWARD, var_list= self.pg_params)


    # TODO REWARD 형태바꾸고 학습하는것 까지 다 구현해보기
    def learn(self, session, state, pvm, reward, state_, pvm_, cash_bias):
        session.run(self.soft_replace)
        _ = session.run(self.atrain, feed_dict = {self.X : state, self.PVM : pvm, self.CASH_BIAS : cash_bias})
        _, summary = session.run([self.ctrain, self.merged], 
                                 feed_dict = {self.X : state, self.PVM : pvm, self.X_ : state_, self.PVM_ : pvm_, self.CASH_BIAS : cash_bias, self.REWARD : reward})
        return summary