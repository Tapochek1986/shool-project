from cryptography.fernet import Fernet

import json
q = Fernet.generate_key()
print(q)
with open('key.key', 'wb') as f:
    f.write(q)
with open('key.key', 'rb') as f:
    key= f.read()
print(key)