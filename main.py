import subprocess
import os
from time import sleep
from includes.config import *
from util.connect import connect_to_api
from util.tools import *
from bases.alerts import Alerts
from subprocess import Popen, PIPE, run,check_output
from ast import literal_eval

# Init Alerts Class
alerts = Alerts(VSTATS_API, connect_to_api, **alerts_context)

# Init Count 
count = 0

# Keep Looping
while True:
    # increment count
    count = count + 1
    # Set defaults
    load = None
    status = None
    space = None
    fn_show = None
        
    try:
        # Get Server Load
        try:
            load = os.getloadavg()
        except Exception as e:
            load = None
        
        
        try:
            # Shard 0 - Remote
            status = getStatus()
        except Exception as e:
            status = None

        try:
            # Shard 0 - Remote
            fn_show = getStatus()
        except Exception as e:
            fn_show = None

        try:
            # Space left
            space = subprocess.check_output('df -BG --output=avail "$PWD" | tail -n 1', shell=True).decode(sys.stdout.encoding)
        except Exception as e:
            space = None
            
        # # Send to vStats
        alerts.send_to_vstats(status, fn_show, load,space,count)
        
    except Exception as e:
        log.error(e) 
        log.error(f"Please fix me!")
        alerts.generic_error(e)
        

    # Delay by x seconds
    #sleep(envs.RUN_EVERY_X_MINUTES * 60)
    sleep(30*60)
    # Hot reload Env
    envs.load_envs()
