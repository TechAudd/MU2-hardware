
RaspberryPi  startup on boot 

sudo apt-get install matchbox-window-manager

#!/bin/bash
matchbox-window-manager &
sleep 2  # Wait for Matchbox to start
python3 /path/to/your_script.py

chmod +x launcher.sh

nano ~/.config/lxsession/LXDE-pi/autostart

@/path/to/launcher.sh

@/home/visveshnaraharisetty/start/match_launcher.sh
@xset s off
@xset -dpms
@xset s noblank



PN532 pi , in desktop 


Create studio .com

sudo lsof /dev/ttyAMA0

sudo apt-get install python3-pil python3-pil.imagetk.  (pillow installation in raspberry pi)

To copy lxsession to lxterminal

cp -r /etc/xdg/lxsession ~/.config/
