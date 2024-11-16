import os

# Configura tus datos de autenticación
ZONE_ID = os.getenv('CF_ZONE_ID')
DNS_RECORD_ID = os.getenv('CF_DNS_RECORD_ID')
API_TOKEN = os.getenv('CF_API_TOKEN')
DNS_NAME = 'pizzapesto.eu'

# Endpoint de Cloudflare
CF_DNS_URL = f'https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{DNS_RECORD_ID}'
