from OpenSSL import crypto
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import config
import base64

# Load PKCS#12 key pair from file
def load_key_pair(p12_file, p12_password):
    with open(p12_file, 'rb') as f:
        p12_data = f.read()
    p12 = crypto.load_pkcs12(p12_data, p12_password)
    private_key = crypto.dump_privatekey(crypto.FILETYPE_PEM, p12.get_privatekey())
    certificate = crypto.dump_certificate(crypto.FILETYPE_PEM, p12.get_certificate())
    return private_key, certificate

# Encrypt data using RSA public key
def encrypt(data, certificate):
    public_key = crypto.load_certificate(crypto.FILETYPE_PEM, certificate).get_pubkey()
    rsa_key = public_key.to_cryptography_key()
    ciphertext = rsa_key.encrypt(data.encode(), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    return ciphertext

# Decrypt ciphertext using RSA private key
def decrypt(ciphertext, private_key):
    rsa_key = crypto.load_privatekey(crypto.FILETYPE_PEM, private_key)
    plaintext = rsa_key.decrypt(ciphertext, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    return plaintext.decode()

# Load PKCS#12 key pair from file
# > openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem
# > openssl pkcs12 -export -in certificate.pem -inkey key.pem -out key.p12
PRIVATE_KEY, CERTIFICATE = load_key_pair('key.p12', config.CertPassword)

# print(f"private Key: {PRIVATE_KEY} , CERT: {CERTIFICATE}")

plainPassword = "1234"
encrypted_password = encrypt(plainPassword, CERTIFICATE)
token = encrypted_password.hex()
print(base64.b64encode(encrypted_password))
print(f"Before Password  {plainPassword} and encrypt to {token}")

expected_password = decrypt(bytes.fromhex(token), PRIVATE_KEY)
#print(f"decrypt password is {expected_password}")