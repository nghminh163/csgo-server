import os
input("required sm and mm first")
ptah="https://ptah.zizt.ru/files/PTaH-V1.1.3-build19-linux.zip"
csgo_path = "csgo-data/csgo/"

def download():
    os.system("wget "+ptah+" -O ptah.zip")

def install():
    os.system("unzip ptah.zip")
    os.system("cp -r addons "+csgo_path)
def clean():
    os.system("rm -rf addons")
    os.system("rm -rf ptah.zip")
    print("Restart server plz and use `sm exts load PTaH`")

download()
install()
clean()