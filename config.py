import os
import hashlib
from dotenv import load_dotenv

load_dotenv()
ServerName = os.getenv('SERVERNAME')
CertPassword = os.getenv('CERT_Password')

ServerNameHash = hashlib.sha256(ServerName.encode('utf-8')).hexdigest()
print(ServerNameHash)