import requests
import os

# Import the variables from the vars.py file
from vars import API_TOKEN, DNS_NAME, CF_DNS_URL

def get_public_ip() -> str:
    """Obtains the public IP of the machine.

    Returns:
        str: The public IP address.
    """
    response = requests.get('https://api.ipify.org?format=json')
    return response.json().get('ip')

def update_dns_record(ip:str) -> dict:
    """Update the DNS record with the new IP.

    Args:
        ip (str): The new IP address.

    Returns:
        dict: The response from the Cloudflare API.
    """
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json',
    }
    data = {
        'type': 'A',
        'name': DNS_NAME,
        'content': ip,
        'ttl': 1,
        'proxied': False,
    }
    response = requests.put(CF_DNS_URL, headers=headers, json=data)
    return response.json()

def main():
    # Obtains the current public IP
    print("Starting the process...")
    print (f"My CF Token is: {API_TOKEN}")
    current_ip = get_public_ip()
    ip_file = '/tmp/current_ip.txt'
    
    # Check if the file exists and read the last IP
    if os.path.isfile(ip_file):
        with open(ip_file, 'r') as f:
            last_ip = f.read().strip()
    else:
        last_ip = None

    # If the IP has changed, update the DNS record
    if current_ip != last_ip:
        # Update the DNS record
        result = update_dns_record(current_ip)
        # Check if the update was successful
        if result['success']:
            print(f"DNS updated: {current_ip}")
            # Store the current IP in a file
            with open(ip_file, 'w') as f:
                f.write(current_ip)
        else:
            print("Error updtaing DNS record", result)
    else:
        print("No changes in the IP.")

if __name__ == "__main__":
    main()
