!!!DISCLAIMER!!! This is just a personal project I did to learn more about how encryption works. This should NOT be used for any real security/encryption purposes.

Instructions:

Generate a key pair, and n (product of primes). a. In terminal, CD into the key_generator folder cd /Users/username/.../Asymmetric_Encryption_Project b. Run python3 key_generators.py and follow the prompts c. A folder called keys with a file called keys.json will be created in the Encrypter_Project folder. It will store your key pairs and n value. NOTE: you only need to generate a key pair once. If the key pair is lost, any encrypted messages will be lost forever. d. You can save key pairs externally to reuse, in case you need to generate another one. Or alternatively modify the code to create multiple key storage files.

Encrypt your messages using encrypt.py a. Once you have your keys and n-value, still in /Users/username/.../Asymmetric_Encryption_Project b. Run python3 encrypt.py and follow the prompts. c. Once you enter your text, a folder called cipher_text with a file called encrypted.json will be created in the Encrypter_Project folder. This file will contain the cipher text of your message and the padding values.

Decrypt your messages using decrypt.py a. When you have ciphertext and padding information in the form of encrypted.json, copy and paste it into to_decrypt.json in the cipher_text folder. b. Still in /Users/username/.../Asymmetric_Encryption_Project, run python3 decrypt.py c. The decrypted text will be output in the terminal.
