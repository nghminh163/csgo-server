import os
input("required sm and mm and ptah first")
wp="https://github.com/kgns/weapons/releases/download/v1.7.0/weapons-v1.7.0.zip"
csgo_path = "csgo-data/csgo/"

def download():
    os.system("wget "+wp+" -O wp.zip")

def install():
    os.system("unzip wp.zip")
    os.system("cp -r cfg "+csgo_path)
    os.system("cp -r addons "+csgo_path)

def clean():
    os.system("rm -rf addons")
    os.system("rm -rf cfg")
    os.system("rm -rf wp.zip")
    print("Restart server plz and use `sm plugins load weapons`")

download()
install()
clean()