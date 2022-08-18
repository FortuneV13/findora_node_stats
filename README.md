# findora Node Stats

## vStatsBot Alerts
- This is an automated script that will periodically ( every 30 mins ) check your node for errors e.g out of sync and alert you via vStatsBot.
- Each alert can be turned on and off via /notifications on vStatsBot.

### Alerts:

If node has fallen out of sync or space then you will get an automatic alert.

You will also get twice daily node summary updates e.g
🔶FRA🔶
In Sync: True
Version: 0.33.9
Latest Block: 2,744,106
Unclaimed FRA: 2,026
Load: 0.21 | 0.32 | 0.28
Space: 59G
Updated: 18 mins ago

Type /nodestats an on demand summary.

## Download the script 
```
cd ~/ && git clone https://github.com/FortuneV13/findora_node_stats && cd findora_node_stats
```

## Automatic Installation:
```
python3 install.py
```
You will need to obtain a token from vStatsBot using the /token command on the bot. The installation script will ask for this token. 

Once complete you should get a ping from vStatsBot to know it installed correctly.

A special thanks to Patrick (Easy Node Validator) for supplying this install script to help speed up the installation process. 

## Manual Installation:
### Get a token
Send the command `/token` to the @vStatsBot on telegram to get your token.

Copy the token, as message on telegram will auto delete after 120 seconds.

### Setup 
Install required packages if missing:
```
sudo apt install python3-pip
pip3 install -r requirements.txt
```
Rename config.example.py to config.py and edit the following variables:
```
cp config.example.py config.py
```

Edit config.py variables ( now support for multiple shards per server):
```
#Add your token from vstats. Run /token on vStatsBot
VSTATS_TOKEN="" 

```
### 4) Test Script 
Test the .env variables and script is working as expected. 

Run the below from the script directory:

```
python3 main.py
```

Alerts on screen AND vStatsBot should appear. Once successful, please cancel the script ( CTRL + C ) and move onto the next step.

## 5) Create Service
Now setup script to run as a service in the background. 

Run the following with sudo privileges. 

```
sudo vi /etc/systemd/system/findora_node_stats.service
```
Copy the below into the service file making sure to edit the User and WorkingDirectory first.
```
[Unit]
Description=findora_node_stats daemon
After=network-online.target

[Service]
Type=simple
Restart=always
RestartSec=1
User=servicefindora
WorkingDirectory=/home/servicefindora/findora_node_stats
ExecStart=python3 main.py
SyslogIdentifier=findora_node_stats
StartLimitInterval=0
LimitNOFILE=65536
LimitNPROC=65536

[Install]
WantedBy=multi-user.target
```
Type `:wq` to save and exit. 

Now enable the service:
```
sudo systemctl daemon-reload
sudo chmod 755 /etc/systemd/system/findora_node_stats.service
sudo systemctl enable findora_node_stats.service
sudo service findora_node_stats start
sudo service findora_node_stats status
```


### Logs
Check logs to make sure the script is running as expected. 

### Misc
Start Service
```
sudo service findora_node_stats start
```

Stop Service
```
sudo service findora_node_stats stop
```
Restart Service
```
sudo service findora_node_stats restart
```

Status Check
```
sudo service findora_node_stats status
```
