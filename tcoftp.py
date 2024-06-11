import ftplib
import re

HOSTNAME = "ftp.jnnprogress.com"
USERNAME = "sanying@jnnprogress.com"
PASSWORD = "Hitachi2023"

# Connect FTP Server
ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
 
# force UTF-8 encoding
ftp_server.encoding = "utf-8"
 
# Enter File Name with Extension
#filename = "File Name"
 
# Read file in binary mode
#with open(filename, "rb") as file:
    # Command for Uploading the file "STOR filename"
#    ftp_server.storbinary(f"STOR {filename}", file)
 
# Get list of files
ftp_server.cwd('images')
ftp_server.dir()

file_names = ftp_server.nlst()
#print(file_names[1])
numberoffile = len(file_names)
pattern = r"ann.\..{3}"
counter = 0
print(file_names)

while counter < len(file_names):
    match = re.search(pattern,file_names[counter])
    if not match:
        file_names.pop(counter)
    else:
        counter = counter +1

print(file_names)

# Close the Connection
ftp_server.quit()