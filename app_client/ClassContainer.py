from ClassLoginForm import LoginForm 
from ClassMenuForm import MenuForm
from ClassRetrieveForm import RetrieveForm
from ClassUploadForm import UploadForm
from pymongo import MongoClient
import ssl

# Set default SSL context to use TLS 1.2
ssl_context = ssl.create_default_context()
ssl_context.set_ciphers('DEFAULT:@SECLEVEL=1')
ssl_context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
url = 'https://phrserver.azurewebsites.net/'
user_attribute = None
