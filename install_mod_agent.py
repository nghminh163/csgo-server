import os
input("required sm and mm and ptah first")
agent="https://github.com/Franc1sco/Franug-AgentsChooser/archive/master.zip"
csgo_path = "csgo-data/csgo/"
folder = "Franug-AgentsChooser-master"
def download():
    os.system("wget "+agent+" -O agent.zip")

def install():
    os.system("unzip agent.zip")
    os.system("mv "+folder+"/*smx "+csgo_path+"addons/sourcemod/plugins")
    os.system("mv "+folder+"/*sp "+csgo_path+"addons/sourcemod/scripting")

def clean():
    os.system("rm -rf "+folder)
    os.system("rm -rf agent.zip")
    print("Restart server plz and use `sm plugins load csgo_voiceagents_enabler` and `sm plugins load csgo_agentschooser`")

download()
install()
clean()