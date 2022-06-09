# importing requried modules

from plyer import battery, notification
import time
from datetime import datetime
import pywhatkit as msg


batteryinfo = battery.status   #this will show the current battery percent  and  whether battery is charging or not
# stored the information in separate variable
info1 = batteryinfo.get("percentage") 
info2 = batteryinfo.get("isCharging") 

now = datetime.now()
hour = int(now.strftime("%H"))
minute = int(now.strftime("%M")) + 1 



while True:
        #checking the condition of battery percent and charging status
        if info1 >= 90 and info2 == True:
                notification.notify(
                        title='NOTIFY',
                        message= f"Battery At {info1}% | Disconnect Charger",
                        app_name='NOTIFY',
                        timeout=10, # the notification will stay on screen for 10 sec
                        app_icon = " " #  download & past the path of the imgae which is in the repo
                    )
                msg.sendwhatmsg('enter your phone number here along with country code', f"Battery At {info1}% | Disconnect Charger", hour, minute)
                print('program finished')
                break
        time.sleep(120) #time has been set so that every 2mins (120sec) the programme will execute, while the contiton is true


