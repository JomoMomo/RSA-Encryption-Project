# Chris Zavik
# This file creates a public and private key pair.

import random
import math
import os
import json

from supporting_scripts.prime_generator import generatePrime
from supporting_scripts.ext_euclid import xgcd
from supporting_scripts.confirm import confirm


###
###  Below we assign p, q, n, and phi
###
print('Processing . . . \n')
p = generatePrime()
q = generatePrime()
while q==p:
    q = generatePrime()

n = p*q

phi = (p-1)*(q-1)

#print('p:   ', p)
#print('q:   ', q)
#print('n:   ', n)
#print('phi:   ', phi)



###
###  Here we choose e such that   2 < e < phi, but we will make the lower range 
### 
def generatePublicKey():
    e = random.SystemRandom().randrange(2**32, (2**64)+1) # ..... we want to choose an e between 2^32 and 2^63 
    while math.gcd(e,phi) != 1: 
        e = random.SystemRandom().randrange(2**32, (2**64)+1) # .......e needs to be such that gcd(e,phi) = 1  ---> i.e. e is coprime to phi 
    return e

###
###  HERE we call private_key_generator(e,phi) to get d - aka the private key
### 
def generatePrivateKey(e,totient):
    d  = xgcd(e,totient)
    return d



    
if __name__=="__main__":

    # Makes a folder to store the generated keys in:


        current_working_dir = os.getcwd()
        #parent_dir = os.path.dirname(current_working_dir)
        folder_name = "keys"
        folder_path = os.path.join(current_working_dir, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        file_name = 'keys.json'
        file_path = os.path.join(folder_path, file_name)
        if os.path.exists(file_path):
            if confirm("\nTHIS WILL OVERWRITE ANY EXISTING KEYS IN THE FILE.\nWe recommend saving your keys externally before proceeding.\nDo you wish to continue? (y/n):\n"):
                print("\nOverwriting File...")
            else:
                print("\nOperation canceled.\n")
                exit()

        public_key = generatePublicKey()
        private_key = generatePrivateKey(public_key, phi)   

        with open(file_path, "w") as file:
            data = {                            # Create a dictionary to hold the key data
                    "public_key": public_key,
                    "private_key": private_key,
                    "n": n
                    }
            json.dump(data, file, indent=4)     # Save the dictionary as a JSON file

        
        test = ((public_key*private_key) % phi)
        if test == 1:
            print("Success.")        
        else:
            print('ERROR: INVALID KEYS. RUN THE SCRIPT AGAIN.')                  
         # The above should always output 1, and if it doesnt, the keys are not mathematically sound. If you get this error message, buy a lottery ticket.