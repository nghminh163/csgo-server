import os
cwd = os.getcwd()
csgo_path = cwd+"/csgo-data"

is_csgo_path = os.path.exists(csgo_path)
if(is_csgo_path==False):
    os.system('mkdir -p '+csgo_path)
    os.system('chmod 777 '+csgo_path)

os.system('docker run -itd  --sig-proxy=false --net=host -v '+csgo_path+':/home/steam/csgo-dedicated/ --name=csgo-dedicated --env-file .env cm2network/csgo')