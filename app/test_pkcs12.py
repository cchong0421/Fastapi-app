import pytest
import config
from OpenSSL import crypto
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
import base64
from pkcs12Demo import load_key_pair, encrypt, decrypt

# Test load_key_pair function
@pytest.mark.parametrize('p12_file, p12_password', [('key.p12', config.CertPassword)])
def test_load_key_pair(p12_file, p12_password):
    private_key, certificate = load_key_pair(p12_file, p12_password)

    assert isinstance(private_key, bytes)
    assert isinstance(certificate, bytes)

# Test encrypt and decrypt functions
# @pytest.mark.parametrize('plain_password', ['1234', 'password', 'test123'])
# def test_encrypt_decrypt(plain_password):
#     PRIVATE_KEY, CERTIFICATE = load_key_pair("key.p12", config.CertPassword)
#     encrypted_password = encrypt(plain_password, CERTIFICATE)
#     token = encrypted_password.hex()
#     expected_password = decrypt(bytes.fromhex(token), PRIVATE_KEY)

#     assert isinstance(encrypted_password, bytes)
#     assert isinstance(expected_password, str)
#     assert expected_password == plain_password

# Run the tests
if __name__ == '__main__':
    pytest.main()