from cryptography.fernet import Fernet

class cryptographer:
    '''
    Cryptography class which 
    - generates a key
    - loads the key
    - encrypts / decrypts a given file with that key
    '''
    def __init__(self):
        self.users = []
        self.key = bytes
    
    def generate_key(self, inFile=False):
        """
        Generates a key
        When using inFile=True it saves the key in a file
        """
        self.key = Fernet.generate_key()

        if inFile:
            print("Generating the key into key.key-file")
            with open("key.key", "wb") as key_file:
                key_file.write(self.key)
        else:
            print("Returning key to caller")
            return self.key


    def load_key(self, fromFile=False):
        """
        Loads the key from the current directory named `key.key`
        """

        if fromFile:
            return open("key.key", "rb").read()
        else:
            self.key


    def encrypt(self, filename, key):
        """
        Encrypting a given file (str) based on a given key (bytes)
        """
        f = Fernet(key)
        
        # read file data
        print("Reading the file ...")
        with open(filename, "rb") as file:
            file_data = file.read()

        # encrypt data
        encrypted_data = f.encrypt(file_data)

        # write encrypted file
        with open(filename, "wb") as file:
            file.write(encrypted_data)


    def decrypt(self, filename, key):
        """
        Decrypting a given file (str) based on a given key (bytes)
        """
        f = Fernet(key)
        
        # read the encrypted data
        print("Reading the encrypted data ...")
        with open(filename, "rb") as file:
            encrypted_data = file.read()

        # decrypt data
        decrypted_data = f.decrypt(encrypted_data)

        # write back original file
        print("Write the decrypted data back ...")
        with open(filename, "wb") as file:
            file.write(decrypted_data)

##################################################
#Workflow

crypto = cryptographer()

# uncomment this if it's the first run and generate the key
key = crypto.generate_key()
# load the key
#key = crypto.load_key()
file = "/user.txt"

import os
from pathlib import Path

currentDirectory = os.path.dirname(__file__)
parentDirectory = os.path.split(currentDirectory)[0]
dataDirectory = parentDirectory + "/data"
userData = dataDirectory + file
print("File is: %s" %userData)

# encrypt the file
crypto.encrypt(userData, key)

# get the file back into the original form:
crypto.decrypt(userData, key)