import hashlib
import ecdsa
import base64

def load_private_key(filename="private_key.bin"):
    """ 从文件加载私钥 """
    with open(filename, "rb") as f:
        private_key = f.read()
    return private_key

def sign_message(private_key, message):
    """ 用私钥对消息进行签名 """
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    message_hash = hashlib.sha256(message.encode()).digest()
    signature = sk.sign(message_hash)
    return base64.b64encode(signature).decode()

def verify_signature(public_key_hex, message, signature_base64):
    """ 验证签名是否有效 """
    public_key_bytes = bytes.fromhex(public_key_hex)
    vk = ecdsa.VerifyingKey.from_string(public_key_bytes, curve=ecdsa.SECP256k1)
    message_hash = hashlib.sha256(message.encode()).digest()
    signature = base64.b64decode(signature_base64)
    try:
        return vk.verify(signature, message_hash)
    except ecdsa.BadSignatureError:
        return False

if __name__ == "__main__":
    message = "This is a test message."
    private_key = load_private_key()
    signature = sign_message(private_key, message)
    print(f"签名: {signature}")
    
    public_key = private_key.hex()  # 这里需要改为正确的公钥转换
    is_valid = verify_signature(public_key, message, signature)
    print(f"签名验证结果: {is_valid}")
