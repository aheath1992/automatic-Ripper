# Automatic ripping from dvd mp4, then saving it to the jellyfin server

#mkv to mp4 convertion 
import subprocess
import os

def convert_mkv_to_mp4(input_mkv_path, output_mp4_path, handbrake_cli_path="HandBrakeCLI"):
    command = [
        handbrake_cli_path,
        "-i", input_mkv_path,
        "-o", output_mp4_path,
        "--preset", "Fast 1080p30" # preset, choose which one works best

    ]
    try:
        print(f"Starting conversion of {input_mkv_path} to {output_mp4_path}...")
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"Conversion successful: {output_mp4_path}")
        print("HandbrakeCLI Output:")
        print(result.stdout)
        if result.stdeer:
            print(f"HandbrakeCLI Errors (if any):")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
         print(f"Error during conversion: {e}")
         print(f"Command: {' '.join(e.cmd)}")
         print(f"Output: {e.stdout}")
         print(f"Error Output: {e.stderr}")
    
    except FileNotFoundError:
        print(f"Error: HandBrakeCLI not found at '{handbrake_cli_path}'. "
              "Ensure it's installed and in your system's PATH or provide the full path.")
    if __name__ == "__main__":
    # Example Usage:
     input_file = "path/to/your/video.mkv"  # Replace with your MKV file path
     output_file = "path/to/your/output.mp4" # Replace with your desired output MP4 path

    # Ensure the input file exists for the example to run
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found. Please provide a valid MKV file.")
    else:
        convert_mkv_to_mp4(input_file, output_file)
        

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
remote_path = 'path/on/server/video.mp4'

try:
    with paramiko.SSHClient() as client:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname,username=username,private_Key_Path=private_Key_Path) 

        with client.open_sftp() as sftp:
            sftp.put(directory_path, remote_path)
            print(f"Successfully uploaded {directory_path} to {remote_path}")

except Exception as e:
    print(f"Error uploading file: {e}")


