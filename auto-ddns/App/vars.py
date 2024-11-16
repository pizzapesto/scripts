import os

# Configura tus datos de autenticación
ZONE_ID = 'zone_id'
DNS_RECORD_ID = 'dns_record_id'
API_TOKEN = os.getenv('CF_API_TOKEN')
DNS_NAME = 'domain.com'

# Endpoint de Cloudflare
CF_DNS_URL = f'https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{DNS_RECORD_ID}'
