# enables the WiFi chip to act as an access point

import network
import time

ap = network.WLAN(network.AP_IF)
ap.active(False) # Reset AP if already running in another mode.
#ap.config(ssid='PicoAP', channel=11, security=network.WLAN.SEC_WPA_WPA2, key='1234567890', pm=network.WLAN.PM_NONE)
ap.config(ssid='PicoAP', channel=11, security=network.WLAN.SEC_OPEN, pm=network.WLAN.PM_NONE)
ap.active(True)

# Wait for the AP to be active
while not ap.active():
    time.sleep(1)
    print("Waiting for AP to be active...")

print("Access point active")
print(ap.ifconfig())

'''
IF_AP                                                                           
IF_STA                                                                          
PM_NONE                                                                         
PM_PERFORMANCE                                                                  
PM_POWERSAVE                                                                    
SEC_OPEN                                                                        
SEC_WPA_WPA2                                                                    
__bases__                                                                       
__dict__                                                                        
active                                                                          
config                                                                          
connect                                                                         
deinit                                                                          
disconnect                                                                      
ifconfig                                                                        
ioctl                                                                           
ipconfig                                                                        
isconnected                                                                     
scan                                                                            
send_ethernet                                                                   
status 
'''
