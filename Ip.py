import requests

def get_ip_details(ip_address):
    """Fetch IP details from ip-api.com"""
    response = requests.get(f"http://ip-api.com/json/{ip_address}")
    data = response.json()

    if data['status'] == 'success':
        return {
            'IP': data['query'],
            'Country': data['country'],
            'Region': data['regionName'],
            'City': data['city'],
            'Latitude': data['lat'],
            'Longitude': data['lon'],
            'ISP': data['isp'],
            'Organization': data['org'],
            'Area Code': data.get('zip', 'N/A'),
            'Country Code': data['countryCode'],
            'ASN': data['as'],
            'Timezone': data['timezone']
        }
    else:
        return {'error': f"Invalid IP: {ip_address}"}

def print_multiple_ip_details(ip_list):
    """Print details for multiple IP addresses"""
    for ip in ip_list:
        details = get_ip_details(ip)
        print(f"\n{'-'*25} IP: {ip} {'-'*25}")
        if 'error' in details:
            print(details['error'])
        else:
            for key, value in details.items():
                print(f"{key}: {value}")

if __name__ == "__main__":
    # Example IP list (you can replace these)
    ip_addresses = [
        "142.250.193.14",  # Google
        "8.8.8.8",         # Google DNS
        "1.1.1.1"          # Cloudflare
        "172.217.194.190"  # Google
    ]
    print_multiple_ip_details(ip_addresses)
