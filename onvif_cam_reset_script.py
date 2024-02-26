# Script for network cam rebooting

from onvif import ONVIFCamera

# Network cam information
username = "" 
password = ""
endpoint = ""
ip = ""
port = ""
wsdl_path = "" # path to onvif-zeep wsdl dyrectory

# Data collection from file. 
# Just comment me out if you don't want to use the configuration via file
try:
    loggin_data = open("cam_config.txt","r") #path to configuration, change me
    for line in loggin_data:
        if 'username' in line:
            username += line[line.index("=")+1:].strip()
        if 'password' in line:
            password += line[line.index("=")+1:].strip()
        if 'wsdl' in line:
            wsdl_path += line[line.index("=")+1:].strip()
        if 'ip' in line:
            ip += line[line.index("=")+1:].strip()
        if 'onvif port' in line:
            port += line[line.index("=")+1:].strip()
except Exception as e:
    print("CONFIGURATION FILE ERROR:", e)
    quit

# Main part - rebooting
try:
    cam = ONVIFCamera(ip, port, username, password, wsdl_path)
    msg = cam.devicemgmt.SystemReboot()
    print(msg)
except Exception as e:
    print("REBOOTING ERROR:", e)
    quit