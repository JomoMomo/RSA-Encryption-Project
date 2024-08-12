import json
import os
import random

from supporting_scripts.confirm import confirm
current_working_dir = os.getcwd()

folder_name = "keys"
file_name = 'keys.json'
file_path = os.path.join(current_working_dir, folder_name, file_name)

with open(file_path, "r") as file:
    keys = json.load(file)

public_key = keys["public_key"]
n = keys["n"]

#print("Public Key:", public_key)
#print("n: ", n)

# Get a message input from the user
message = input("Enter your message: ")

# Convert the message to its ASCII representation and salt it up
ascii_values = []
padding_values = []
for char in message:
    padding = random.randint(1, 1000)
    ascii_padded = ord(char) + padding
    ascii_values.append(ascii_padded)
    padding_values.append(padding)

# The math for getting cipher text 'c' from a plaintext message 'm' is c = (m^public_key)(modn)
cipher_text = [pow(char, public_key, n) for char in ascii_values]



#print("Padded ASCII values:", ascii_values)
#print("Padding values:", padding_values)
#print("Ciphertext: ", cipher_text)


#Below we instantiate another folder that stores the ciphertext along with the padding values.
current_working_dir = os.getcwd()
folder_name = "cipher_text"
folder_path = os.path.join(current_working_dir, folder_name)
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

file_name = 'encrypted.json'
file_path = os.path.join(folder_path, file_name)
if os.path.exists(file_path):
    if confirm("\nTHIS WILL OVERWRITE ANY EXISTING CIPHERTEXT AND PADDING VALUES IN THE FILE.\nIf it will be needed in the future, save the file externally before proceeding,.\nDo you wish to continue? (y/n):\n"):
        print("\nOverwriting Ciphertext...")
    else:
        print("\nOperation canceled.\n")
        exit()


with open(file_path, "w") as file:
    data = {                            # Create a dictionary to hold the CipherText and Padding Values
            "Encrypted Cipher Text": cipher_text,
            "Padding Values": padding_values
            }
    json.dump(data, file, indent=4) 

if os.path.exists(file_path):
    print("\nCiphertext successfuly written to Asymmetric_Encryption_Project/cipher_text/encrypted.json\n")
else:
    print('Error writing ciphertext. Please Try again.')


