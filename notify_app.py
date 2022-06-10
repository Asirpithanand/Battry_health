# importing requried modules

import urllib.request
from plyer import battery, notification
import time
from datetime import datetime

def wifi(host='http://google.com'):
    """chekcing the connection of internet via google search as google is reliable"""
    try:
        urllib.request.urlopen(host)  
        return True
    except:
        return False
connected = wifi()

if connected == True:
    import pywhatkit as msg


batteryinfo = battery.status   #this will show the current battery percent  and  whether battery is charging or not
# stored the information in separate variable
info1 = batteryinfo.get("percentage") 
info2 = batteryinfo.get("isCharging") 

now = datetime.now()
hour = int(now.strftime("%H"))
minute = int(now.strftime("%M")) + 1 


while True:
        if info2 == False:
            notification.notify(
                        title='NOTIFY',
                        message= f"Battery At | {info1}%",
                        app_name='NOTIFY',
                        timeout=10, # the notification will stay on screen for 10 sec
                        app_icon = " "  # copy and paste the path of the image attached with this repo
                    )
            break    

        #checking the condition of battery percent and charging status
        elif info1 >= 90 and info2 == True:
                if connected == True:
                    msg.sendwhatmsg('enter your whatsapp number here along with country code', f"Battery At {info1}% | Disconnect Charger", hour, minute)
                elif connected == False:
                    notification.notify(
                        title='NOTIFY',
                        message= f"Battery At {info1}% | Disconnect Charger",
                        app_name='NOTIFY',
                        timeout=10, # the notification will stay on screen for 10 sec
                        app_icon = " " # copy and paste the path of the image attached with this repo
                    )
                    break
                print('program finished')
                break
        time.sleep(120) #timer has been set so that every 2mins (120sec) the program will execute, while the contiton is true


