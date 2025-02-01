import os
import hashlib
import ecdsa
import base64
import qrcode

def generate_private_key():
    """ 生成 1024 比特随机私钥，并取 SHA256 哈希前 32 字节 """
    raw_key = os.urandom(128)  # 生成 1024 比特随机数
    private_key = hashlib.sha256(raw_key).digest()  # 取 SHA256 哈希
    with open("private_key.bin", "wb") as f:
        f.write(private_key)  # 保存私钥到 .bin 文件
    return private_key.hex()

def private_to_public(private_key_hex):
    """ 从私钥计算公钥（secp256k1） """
    private_key_bytes = bytes.fromhex(private_key_hex)
    sk = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    public_key = b'\x04' + vk.to_string()  # 添加 04 作为非压缩格式标识
    return public_key.hex()

def public_to_address(public_key_hex):
    """ 计算公钥哈希并生成 Base64 编码的地址 """
    public_key_bytes = bytes.fromhex(public_key_hex)
    sha256 = hashlib.sha256(public_key_bytes).digest()
    ripemd160 = hashlib.new('ripemd160', sha256).digest()
    address_bytes = b'\x00' + ripemd160  # 添加 00 作为前缀
    address = base64.b64encode(address_bytes).decode()  # 使用 Base64 替代 Base58
    return address

def generate_qr_code(data, filename="address_qr.png"):
    """ 生成二维码图片 """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"二维码已保存为 {filename}")

if __name__ == "__main__":
    private_key = generate_private_key()
    public_key = private_to_public(private_key)
    address = public_to_address(public_key)
    
    print(f"私钥已保存至 private_key.bin")
    print(f"公钥: {public_key}")
    print(f"地址: {address}")
    
    generate_qr_code(address)
