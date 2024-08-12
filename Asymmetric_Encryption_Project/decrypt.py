import json
import os
from supporting_scripts.confirm import confirm

if confirm("\nIs the ciphertext and padding in /cipher_text/to_decrypt.json?(y/n):\n"):
    print("\nThe Decrypted message is:")
else:
    print("\nPlease paste the json of the ciphertext and padding into /cipher_text/to_decrypt.json and then run the program again.\n")
    exit()

# Below we import and store the ciphertext and the padding values.
current_working_dir = os.getcwd()

folder_name = "cipher_text"
file_name = 'to_decrypt.json'
file_path = os.path.join(current_working_dir, folder_name, file_name)

with open(file_path, "r") as file:
    to_decrypt = json.load(file)

ciphertext = to_decrypt["Encrypted Cipher Text"]
padding = to_decrypt["Padding Values"]

#print(ciphertext)
#print(padding)


# Below we import and store the private key and the n-value.
folder_name = "keys"
file_name = 'keys.json'
file_path = os.path.join(current_working_dir, folder_name, file_name)

with open(file_path, "r") as file:
    keys = json.load(file)

private_key = keys["private_key"]
n = keys["n"]
#print('n: ',  n)
#print('Private Key: ', private_key)

ascii_and_pad = [pow(char, private_key, n) for char in ciphertext]  # The math for decrypting FROM ciphertext 'c' TO a plaintext message 'm' is m = (c^private_key)(modn)
#print(ascii_and_pad)


ascii_values = [a - b for a, b in zip(ascii_and_pad, padding)] # Unpadding
#print(ascii_text)

plain_text = ''.join(chr(value) for value in ascii_values)
print(plain_text, "\n")