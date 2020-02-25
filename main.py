from fernet import Fernet
import string
import random
import base64
key = b'' # Generates key to be stored on the lock and is unique to each lock

message = b''
def getMessage():
  global message
  message = bytes(input("What would you like to encode? ").encode('utf-8')) # "What would you like to encode? " will be replaced with the NFC Tag


def writeKey(): 
  global key 
  key = Fernet.generate_key()
  file = open('key.key', 'wb')
  file.write(key) # The key is type bytes still
  file.close()

#Generates Pin to be displayed on phone and punched into keypad (currently written to file)

def randomPin(pinLength):
  """Generate a random string of fixed length """
  numbers = ['0','1','2','3','4','5','6','7','8','9']
  file = open('pin.key', 'wb')
  pin = ''.join(random.choice(numbers) for i in range(pinLength))
  print(pin)
  pin = bytearray(pin, 'utf-8')
  pin = base64.b64encode(pin)
  file.write(pin)
  file.close()



# Generates key to be written to NFC Tag but is currently written to file

def readKey():
  global key
  file = open('key.key', 'r')
  key = file.read()
  file.close()

def printKey():
  print(key)

def encrypt():
  f = Fernet(key)
  encrypted = f.encrypt(message)
  file = open('encrypted.txt', 'wb')
  file.write(encrypted)
  file.close()
    

def decrypt():
  file = open('encrypted.txt', 'rb')  
  encrypted = file.read()
  f = Fernet(key)
  decrypted = f.decrypt(encrypted)
  print(decrypted.decode('utf-8'))

def key():
  readKey()
  printKey()