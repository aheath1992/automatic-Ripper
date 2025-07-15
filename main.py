# Automatic ripping from dvd mp4, then saving it to the jellyfin server

# looking for mp4 files 
import glob

# specific directory
directory_path = "path/to/you/directory"
mp4_files = glob.glob(f'{directory_path}/*.mp4')

#process the results
for file_path in mp4_files:
    print (file_path)

# moving mp4 to jellyfin server
import paramiko

hostname = "jf1.example.com"
username = "root"
private_Key_Path = 'path/to/your.private_key'
local_path = 'path/to/your/local/video.mp4'
remote_path = 'path/on/server/video.mp4'

try:
    with paramiko.SSHClient() as client:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname,username=username,private_Key_Path=private_Key_Path) 

        with client.open_sftp() as sftp:
            sftp.put(local_path, remote_path)
            print(f"Successfully uploaded {local_path} to {remote_path}")

except Exception as e:
    print(f"Error uploading file: {e}")


