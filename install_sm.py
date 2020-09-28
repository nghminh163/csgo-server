import os


source_mod = "https://sm.alliedmods.net/smdrop/1.10/sourcemod-1.10.0-git6497-linux.tar.gz"
mm_source="https://mms.alliedmods.net/mmsdrop/1.10/mmsource-1.10.7-git971-linux.tar.gz"

def download():
    os.system("wget "+source_mod+" -O sm.tar.gz")
    os.system("wget "+mm_source+" -O mms.tar.gz")

def install():
    os.system("tar -zxvf sm.tar.gz")
    os.system("tar -zxvf mms.tar.gz")
    os.system("mv addons csgo-data/csgo")
    os.system("mv cfg/sourcemod csgo-data/csgo/cfg")

def clean():
    os.system("rm -rf sm.tar.gz")
    os.system("rm -rf mms.tar.gz")
    os.system("rm -rf cfg")

download()
install()
clean()
print("Restart server plz")