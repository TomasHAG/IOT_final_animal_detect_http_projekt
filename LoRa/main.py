import detector
import time
import light_manager

def lora_cb(lora): # initilize logic for callback to get and send packages.
    events = lora.events()

    if events & LoRa.TX_PACKET_EVENT: # send package with trigger
        light_manager.data_send()

# activate callbacks
lora.callback(trigger=(LoRa.TX_PACKET_EVENT), handler=lora_cb)

def send(port, pin): # send wether data from memory to a specifik port
    s.bind(port) # bind to the new port
    s.send(bytes([pin])) # send a trigger payload

def loop(): # internal loop to detect and send data
    counter = 0
    while True:
        time.sleep(2) # loop in 2 sec intervalls
        counter += 1
        pin, trigger = detector.read()
        if trigger:
            send(2, pin) # send in port 2 that an animal have ben detected
            time.sleep(1*30) # after detection trigger sleep for 1 minute
            counter = 0 # reset echo counter
        elif counter > 10*30: # every 10 minutes
            send(3, 0xFF) #port 3 is for echo calls
            counter = 0 # reset echo counter

loop()
