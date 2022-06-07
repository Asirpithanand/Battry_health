from plyer import battery, notification
import time

while True:
        batteryinfo = battery.status   
        # stored the information in separate variable
        info1 = batteryinfo.get("percentage") 
        info2 = batteryinfo.get("isCharging") 

        #checking the condition of battery percent and charging status
        if info1 >= 90 and info2 == True:
                notification.notify(
                        title='NOTIFY',
                        message= f"Battery At {info1}% | Disconnect Charger",
                        app_name='NOTIFY',
                        timeout=10, # the notification will stay on screen for 10 sec
                        app_icon = "D:\Programing\Language\Python\Projects\Battery Health\Oxygen-Icons.org-Oxygen-Status-battery-charging.ico" #copy the path of the imgae and paste here
                    )
                time.sleep(120) #time has been set so that every 2mins (120sec) the programme will execute, while the contiton is true

        elif info2 == False: # this condition is to make sure the programme has been ended 
            print(batteryinfo)
            print('Programme finished')
            break # because this elif condition  is inside a while loop it is important to break the loop after the programme is executed 
        
