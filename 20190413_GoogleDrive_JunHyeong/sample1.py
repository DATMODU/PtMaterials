# -*- coding: utf-8 -*-
import io
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http

SERVICE_ACC_KEY_FILE_NAME = "service_acc_key.json"
SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
FILE_ID = "1EFzqg-bfKXOjHP3q7NNUM6QYuEln8sR5"

credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACC_KEY_FILE_NAME, SCOPES)

http_auth = credentials.authorize(Http())
drive = build("drive", "v3", http=http_auth)

print("\nMetaData:")
response = drive.files().get(fileId=FILE_ID).execute()
print(response)

print("\nDownload Start")
request = drive.files().get_media(fileId=FILE_ID)
buffer = io.BytesIO()
downloader = MediaIoBaseDownload(buffer, request)
done = False

while done is False:
	status, done = downloader.next_chunk()
	print("Download %d%%." % int(status.progress() * 100))

print("Download Result:")
print(buffer.getvalue())
