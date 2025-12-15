from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Hash import SHA256
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad
import base64

password = "123PetitsChats"
salt_base64 = "JR53k2vFWO11bPrXZLcCYEE01fxSQhTy/8oWaco0bIs="
cipher_base64 = "aGQt3HsqhFFf886oMWW9D0jGr7EiTZYSL1o29fwTp0Zg8U9V/KPM+VVfq86aCZxhRWS0XoLXLAtn+RCmysOWs04hNHRI7h87zAIpgIpIlpCgX2KEaAa+h3imQ9uueSLzpjxOijiCVwc69eqTJtntbr2dlgFM6nG6a62OLDa+A/XaiBBc2pzcp42DyReTccaAqbcUk6RknbLhDxjCcg4V+Eeocu3mJVpqlvKsl7wud4xJt0qXVaYf9sNWBrmWNGSzS8ta5aPI+/ypZveV7Hq0kBHJN6tVaGT800oElguxKr9p5xMO4WJPny6x32qNAbLGKZaG3E1BqvjT04aYY/P7NX05jNXYu6g43OSGVSxNg2dPeYAGEsSBbc6N++pUAJ935Ht9LcEtYWn9QRA31xxel7s/Nn6c+CVWNVZvLway0x9w9qr+S3Ra9M5WC4TP7EjfK1F8qJ093dHSXv/IfknsFa+AAszlIOVlBIqF7ONJ20zi2KFkFq7aPipNg0BDysFAO4QwcpqNgQlnV5ycrX6XXRWH+8OkMpHTO9XmP4XVmObtOG4GFjrCXjhRjxR04X4rJ7FNRYSO7mjDDv1rCe9itJS2T8mrNtDzKwKfq0FrLhatNoAv51m4q91xtl6UKFqEaef7u3xx/RyQc8kyGGtHUmEr9IlLJMxDsUwkqRtDFnOK0YIhpsAKpIKv1ZBHbORk+L/qn5M208ZHhWz3ZMLa0I3Bdbocngv37C+YT6l3pXAaRxy/yyWSRWCypKwdoAx6SFC7r9sChfbjosEvYn+2eFjERjcWa7PCj8DVFsg6eFagLRJxdoHAGuckCrT3iMGoFSRo1erjB1zz5J+XifBnetX72vJh9F+RboLQh8axXkgs6w10YdZApUg9pGC+7VNBRRofs+N8fg9KK3euxIcwjQZzySf+9SxZSeUF+EpnIxDVTEPrQetcyHiWK9/j2XwEQAKmLPLW/BiVHQROQmv80mDWdJudeVG6wJ9WZqmacnJM4WTop1VbAZlw+nfjF3A4Xok0dZyQNbBb+NJFrqjDPLCJ/G1aIym6EyFlppHF8O/gG+MgE0elsqLLWmM5lu132+fZCHr4E97x/1NvMuiIe9QrhEr/A3E3QvJ5b45JwJYmVsyoqAYK+oMh8xoNUxVhbdbA3g4YQPZdgF2JQ1iXNN4C4aHfPpyOyt/rxW1e4UGkXjYeqn0an2tSVjIJQZvioL+cbQ1uaWtvrb/MrgeOXv4KhMsyq61xZjSdGglGYzAGueSUPwZ3rSZtj8ePhFXfCzIULByiuQ1Y2uRzDtHs5FSpuhJqAmxyui9dM60pFyaYNEltI7wdyYBRz6DutuBEhtVP5wYiKdvZBoHfJ8KOjtlbRfv9XCkyBeaCWOXQkua6Kj+69RQz32TS3gNceZaxFP5jbvFXrCA18At3dw4Ojn6IisHEeFkCEdrsYCxCOOOT67jl5jkm9bofZgM0S63f0jkD0IShmgGC7Nvaz/noM+JxbOvfwBUNEFHj5ZrOgMcxmbduCvn220UQFWRpy5+ZJ2gu1SSC7w=="
iv_base64 = "V52NqKHOL8C0jbNYOHItgw=="
salt = base64.b64decode(salt_base64)

# Dériver la clé avec PBKDF2
key = PBKDF2(
    password=password.encode("utf-8"),
    salt=salt,
    dkLen=32,  # 256 bits = 32 bytes
    count=600000,  # iterations
    hmac_hash_module=SHA256
)

print("=== PARAMÈTRES DE DÉRIVATION DE CLÉ ===")
print(f"Password: {password}")
print(f"Salt (Base64): {salt_base64}")
print(f"Salt (hex): {salt.hex()}")
print(f"Derived Key (hex): {key.hex()}")
print(f"Derived Key (Base64): {base64.b64encode(key).decode()}")


ciphertext = base64.b64decode(cipher_base64)
iv = base64.b64decode(iv_base64)

print("\n=== DÉCHIFFREMENT DES DONNÉES ===")
print(f"IV (hex): {iv.hex()}")
print(f"Encrypted data length: {len(ciphertext)} bytes")

print("\n=== DONNÉES DÉCHIFFRÉES ===")
cipher = AES.new(key, AES.MODE_GCM, iv)
decrypted_raw = cipher.decrypt(ciphertext)
print(decrypted_raw)

print("\n=== Mnemonic ===")
mnemonic = [110,97,112,107,105,110,32,115,116,97,105,114,115,32,97,108,108,111,119,32,116,114,97,112,32,108,105,103,104,116,32,99,97,117,116,105,111,110,32,115,99,105,115,115,111,114,115,32,99,97,115,104,32,116,121,112,105,99,97,108,32,119,105,110,116,101,114,32,98,101,116,116,101,114,32,99,104,97,105,114]
mnemonic_str = ''.join(chr(i) for i in mnemonic)
print(mnemonic_str)

