import os
input("required sm and mm and ptah first")
pug="https://github.com/splewis/csgo-pug-setup/releases/download/2.0.5/pugsetup_2.0.5.zip"
csgo_path = "csgo-data/csgo/"
def download():
    os.system("wget "+pug+" -O pug.zip")

def install():
    os.system("unzip -o pug.zip")
    os.system("mv addons/sourcemod/plugins/disabled/pugsetup_teamnames.smx addons/sourcemod/plugins")
    os.system("mv addons/sourcemod/plugins/disabled/pugsetup_chatmoney.smx addons/sourcemod/plugins")
    os.system("mv addons/sourcemod/plugins/disabled/pugsetup_damageprinter.smx addons/sourcemod/plugins")
    os.system("cp -r cfg "+csgo_path)
    os.system("cp -r addons "+csgo_path)


def clean():
    os.system("rm -rf addons")
    os.system("rm -rf pug.zip")
    os.system("rm -rf cfg")
    print("Restart server plz and use `sm plugins load pugsetup` `sm plugins load pugsetup_teamnames` `sm plugins load pugsetup_chatmoney` `sm plugins load pugsetup_damageprinter`")

download()
install()
clean()