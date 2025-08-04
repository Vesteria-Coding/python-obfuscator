import os
import base64

# Setup
with open('code.py', 'r') as file:
    code = file.read()

obfuscated_code = []
deobfuscated_code = ''
base64_encoded = ''

# Encode to Base64
code = code.encode("ascii")
base64_encoded = base64.b64encode(code)
base64_encoded = base64_encoded.decode('ascii')
code = code.decode("ascii")

# Encode to ACSII
for i in base64_encoded:
    obfuscated_code.append(ord(i))

# Write to file
with open('obfuscated_code.py', 'w') as out:
    out.write('import base64; ')
    out.write(f'obfuscated_code = {obfuscated_code}; ')
    out.write('deobfuscated_code = "".join([chr(i) for i in obfuscated_code]); ')
    out.write('exec(base64.b64decode(deobfuscated_code))')