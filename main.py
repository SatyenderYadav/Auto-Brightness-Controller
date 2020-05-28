import psutil
import wmi

#brightness control function 
def brightness(value):
    brightness = value # percentage [0-100]
    c = wmi.WMI(namespace='wmi')
    methods = c.WmiMonitorBrightnessMethods()[0]
    methods.WmiSetBrightness(brightness, 0)
    
#Give Battery percentage     
battery = psutil.sensors_battery()
percent = (battery.percent)

if percent == 100:
    brightness(100)
elif percent < 100 and percent >= 90 :
    brightness(90)
elif percent < 90 and percent >= 80 :
    brightness(80)
elif percent < 80 and percent >= 60 :
    brightness(60)
elif percent < 60 and percent >= 0 :
    brightness(40)

     
