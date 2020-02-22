from fernet import Fernet
import string
import random


# Generates key to be written to NFC Tag but is currently being written to a file

def writeKey():
    key = Fernet.generate_key()
    file = open('key.key', 'wb')
    file.write(key) # The key is type bytes still
    file.close()

#Generates Pin to be displayed on phone and punched into keypad
def randomString(pinLength):
    """Generate a random string of fixed length """
    numbers = [0,1,2,3,4,5,6,7,8,9]
    return ''.join(str(random.choice(numbers)) for i in range(pinLength))


