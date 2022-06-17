# importing all the requried modules and packages
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


while True:

    connected = wifi()

    if connected == True: #importing this module without internet it will raise an error to avoid it an if conndition has been set
        import pywhatkit as msg

    now = datetime.now()
    hour = int(now.strftime("%H"))
    minute = int(now.strftime("%M")) + 2 # Call Time must be Greater than Wait Time as WhatsApp Web takes some Time to Load! That's why we have added 2 to the current time

    batteryinfo = battery.status   #this will show the current battery percent  and  whether battery is charging or not
    # stored the information in separate variable
    info1 = batteryinfo.get("percentage") 
    info2 = batteryinfo.get("isCharging") 

    # this if block will execute only when laptop is not charging
    if info2 == False:
        notification.notify(
                    title='NOTIFY',
                    message= f"Battery At | {info1}% Remaining",
                    app_name='NOTIFY',
                    timeout=10, # the notification will stay on screen for 10 sec
                    app_icon = " "  # copy and paste the path of the image attached with this repo
                )
        print('Program Finished')
        break    

    #checking the condition of battery percent and charging status
    elif info1 >= 89 and info2 == True: # You can edit the number & set number according to your need 
            if connected == True: # only if the laptop has internet connection this if block will execute and send message to whatsapp
                msg.sendwhatmsg('enter your mobile number along with country code', f"Battery At {info1}% | Disconnect Charger", hour, minute)

            elif connected == False: # if not connected to internet normal notification will pop up
                notification.notify(
                    title='NOTIFY',
                    message= f"Battery At {info1}% | Disconnect Charger",
                    app_name='NOTIFY',
                    timeout=10, # the notification will stay on screen for 10 sec
                    app_icon = " " # copy and paste the path of the image attached with this repo
                )
            print('Program Finished')
            break
        
    time.sleep(120) #timer has been set so that every 2mins (120sec) the program will execute, while the contiton is true


