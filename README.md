# findora Node Stats

## vStatsBot Alerts
- This is an automated script that will periodically ( every 30 mins ) send your node data to vStats for dashboard + alerts.
- Each alert can be turned on and off on a node by node basis ( via .env ) or globally via /notifications on vStatsBot.

### Dashboard:

Shows your node stats on a single page.

Unique page can be found by running /nodestats in vStatsBot

Example dashboard https://vstats.test/node-stats/example

### Alerts:

Node summary request. Type /nodestats for a server summary. These are also scheduled daily. 

## Data Collected
- Findora Utility Metadata 
- Hostname
- Server Load
- Server Space in current filesystem

## Pre Installation Notes
- Script must be installed on each individual node

## Installation 

### 1) Download the script
We suggest storing it in your home folder.

```
cd ~/
git clone https://github.com/FortuneV13/findora_node_stats
cd findora_node_stats
```
To update use `git pull`

Install required packages if missing:

<!-- `sudo apt update && sudo apt upgrade -y` -->
```
sudo apt install python3-pip
pip3 install -r requirements.txt
```

### 2) Get a token
Send the command `/token` to the @vStatsBot on telegram to get your token.

Copy the token, as message on telegram will auto delete after 120 seconds.

### 3) Setup 
Rename .env.example to .env and edit the following variables:
```
cp .env.example .env
nano .env
```
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
