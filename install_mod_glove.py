import os
input("required sm and mm and ptah first")
glove="https://github.com/kgns/gloves/releases/download/v1.0.4/gloves-v1.0.4.zip"
csgo_path = "csgo-data/csgo/"

def download():
    os.system("wget "+glove+" -O glove.zip")

def install():
    os.system("unzip glove.zip")
    os.system("cp -r cfg "+csgo_path)
    os.system("cp -r addons "+csgo_path)

def clean():
    os.system("rm -rf addons")
    os.system("rm -rf cfg")
    os.system("rm -rf glove.zip")
    print("Restart server plz and use `sm plugins load weapons`")

# download()
install()
clean()