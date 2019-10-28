import os
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from google.colab import auth
from oauth2client.client import GoogleCredentials


def export_folder(filename, out_drive_folder_id):
  '''Export colab folder to drive folder '''
  file = drive.CreateFile({"parents": [{"kind": "drive#fileLink",
                                        "id": out_drive_folder_id}]})
  # Zip folder
  #!echo '/content/sample_data'
  cmd = "zip -r out.zip " + filename 
  returned_value = os.system(cmd)
  print('returned value:', returned_value)
  
  # Export file
  file.SetContentFile('out.zip')#
  file.Upload() 
  #!rm out.zip
  return True



# Authenticate and create the PyDrive client.
# This only needs to be done once per notebook.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

weights_name = '/content/darknet/backup'
out_drive_folder_id = '1LvWCZ5hX7xjnRV0_p9w22f4zsg12Qzxx'
export_folder(weights_name, out_drive_folder_id)
