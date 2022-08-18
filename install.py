import os
import sys
from os import environ

userHomeDir = os.path.expanduser("~")
activeUserName = os.path.split(userHomeDir)[-1]

def askYesNo(question: str) -> bool:
    YesNoAnswer = ""
    while not YesNoAnswer.startswith(("Y", "N")):
        YesNoAnswer = input(f"{question}: ").upper()
    if YesNoAnswer.startswith("Y"):
        return True
    return False


def updateTextFile(fileName, originalText, newText):

    with open(fileName,'r') as f:
        filedata = f.read()

    newdata = filedata.replace(originalText, newText)

    with open(fileName, 'w') as f:
        f.write(newdata)


def installVstats(vstatsToken) -> None:
    os.system("sudo service findora_node_stats stop")
    os.system(f"sudo rm -r {userHomeDir}/findora_node_stats")
    # Install it bud, pull git repo
    os.chdir(f"{userHomeDir}")
    os.system("git clone https://github.com/FortuneV13/findora_node_stats")
    os.chdir(f"{userHomeDir}/findora_node_stats")
    # setup python stuff
    os.system("sudo apt install python3-pip -y")
    os.system("pip3 install -r requirements.txt")
    # customize config file
    os.system("cp config.example.py config.py")
    updateTextFile(f"{userHomeDir}/findora_node_stats/config.py", 'VSTATS_TOKEN=""', f'VSTATS_TOKEN="{vstatsToken}"')
    # Do service stuff here
    if activeUserName == 'root':
        os.system(
        f"sudo cp {userHomeDir}/findora_node_stats/util/findora_node_stats.service . && sed -i 's/home\/servicefindora/{activeUserName}/g' 'findora_node_stats.service' && sed -i 's/servicefindora/{activeUserName}/g' 'findora_node_stats.service' && sudo mv findora_node_stats.service /etc/systemd/system/findora_node_stats.service && sudo chmod a-x /etc/systemd/system/findora_node_stats.service && sudo systemctl enable findora_node_stats.service && sudo service findora_node_stats start"
    )
    else:
        os.system(
        f"sudo cp {userHomeDir}/findora_node_stats/util/findora_node_stats.service . && sed -i 's/servicefindora/{activeUserName}/g' 'findora_node_stats.service' && sudo mv findora_node_stats.service /etc/systemd/system/findora_node_stats.service && sudo chmod a-x /etc/systemd/system/findora_node_stats.service && sudo systemctl enable findora_node_stats.service && sudo service findora_node_stats start"
    )
    return
    

def getToken():
    if len(sys.argv) > 1:
        vstatsToken = sys.argv[1]
    else:
        vstatsToken = input(
            f"* Please input your vStats token here: "
        )
    return vstatsToken


if __name__ == '__main__':
    os.system("clear")
    # Check for argument token or ask for one!
    vstatsToken = getToken()
    
    # install once we have the info to customize
    installVstats(vstatsToken)

    # Goodbye!
    print("****")
    print("\n*\n* Installer has finished, you should have a ping waiting on vStats if everything was input correctly\n* You can also run `sudo service findora_node_stats status` to verify your service is online and running!\n*")
    print("****")
