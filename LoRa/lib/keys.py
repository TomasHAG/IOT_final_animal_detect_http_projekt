import ubinascii
# Here are the keys that are used to initilize LORAWAN
def eui():
    return ubinascii.unhexlify('your EUI key here')

def key():
    return ubinascii.unhexlify('your API key here')
