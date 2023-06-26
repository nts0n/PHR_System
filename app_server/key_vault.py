from dotenv import load_dotenv
import os
from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential


load_dotenv()

TENANT_ID = os.getenv('AZURE_TENANT_ID')
CLIENT_ID = os.getenv('AZURE_CLIENT_ID')
CLIENT_SECRET = os.getenv('AZURE_CLIENT_SECRET')


credential = ClientSecretCredential(
    tenant_id=TENANT_ID,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)


url = "https://phr-key.vault.azure.net//"
secret_client = SecretClient(vault_url=url, credential=credential)

#secret_name = "master-key"

# secret_name = "Secret1"
#secret = secret_client.get_secret(secret_name)
#secret_value = secret.value
#print(secret_value)
