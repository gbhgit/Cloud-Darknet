import os
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from google.colab import auth
from oauth2client.client import GoogleCredentials

import time
import datetime

def export_folder(filename, out_drive_folder_id):
  '''Export colab folder to drive folder '''
  file = drive.CreateFile({"parents": [{"kind": "drive#fileLink",
                                        "id": out_drive_folder_id}]})
  # Zip folder
  #!echo '/content/sample_data'
  new_name = get_filename()
  cmd = "zip -r out-{}.zip ".format(new_name) + filename 
  returned_value = os.system(cmd)
  print('returned value:', returned_value)
  
  # Export file
  file.SetContentFile('out-{}.zip'.format(new_name))#
  file.Upload() 
  #!rm out.zip
  return True

def get_filename():
  ts = time.time()
  st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M')
  return st


# Authenticate and create the PyDrive client.
# This only needs to be done once per notebook.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

weights_name = '/content/darknet/backup'
#out_drive_folder_id = '1LvWCZ5hX7xjnRV0_p9w22f4zsg12Qzxx'
out_drive_folder_id = os.environ.get('OUTPUT_FOLDER_ID')
export_folder(weights_name, out_drive_folder_id)
