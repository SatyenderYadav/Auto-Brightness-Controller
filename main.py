import wmi

brightness = 100 # percentage [0-100]
c = wmi.WMI(namespace='wmi')

methods = c.WmiMonitorBrightnessMethods()[0]
methods.WmiSetBrightness(brightness, 0)

 