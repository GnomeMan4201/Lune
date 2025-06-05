import base64
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

SECRET_KEY = b'LUNESECRETKEY123'  # 16 bytes key for AES-128

def encrypt_message(data):
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(json.dumps(data).encode(), AES.block_size))
    return base64.b64encode(cipher.iv + ct_bytes).decode()

def decrypt_message(token):
    raw = base64.b64decode(token)
    iv = raw[:AES.block_size]
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(raw[AES.block_size:]), AES.block_size)
    return json.loads(pt.decode())
