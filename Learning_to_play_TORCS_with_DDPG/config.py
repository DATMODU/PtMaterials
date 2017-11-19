# MODEL Hyperparameter

PRETRAIN_STEPS = 1e+6       # Total training period in the paper
TAU = 0.1                  # Soft replacement hyperparameter
REGULIZE_COEFF = 1e-8       # L2 regularization coefficient
LEARNING_RATE = 3e-5        # Learning rate
PRESELET_DAYS = 30          # Trading volume observing period to preselect alt coins
COMMISION_RATE = 0.0025     # Trading cost in exchange
DELTA = 0.0001              # Maximum error when calculating mu_t (portfolio rebalacning cost constant)
EXPLORATION_EPS = 0.5
EXPLORATION_PERIOD = 5e+4

# Trainig Options
TRAINING = True

