# IPaddressFinder
Multi IP Address Lookup
This Python script fetches location and network details for one or more IP addresses using the free ip-api.com service.

Features
Get Country, Region, City for an IP address

Shows Latitude, Longitude, ISP, Organization

Works with multiple IPs at once

No API key required

Requirements
Python 3.x

requests library

Install the required library:

bash
Copy
Edit
pip install requests
Usage
Clone or download this script.

Edit the ip_addresses list in the script and add the IPs you want to check.

Run the script:

bash
Copy
Edit
python multi_ip_lookup.py
Example Output
yaml
Copy
Edit
------------------------- IP: 142.250.193.14 -------------------------
IP: 142.250.193.14
Country: United States
Region: California
City: Mountain View
Latitude: 37.4056
Longitude: -122.0775
ISP: Google LLC
Organization: Google LLC
Area Code: 94043
Country Code: US
ASN: AS15169 Google LLC
Timezone: America/Los_Angeles

------------------------- IP: 8.8.8.8 -------------------------
IP: 8.8.8.8
Country: United States
Region: California
City: Mountain View
...
Notes
This script uses ip-api.com which has a free tier limit of 45 requests per minute.

Make sure to include commas between IP addresses in the list:

python
Copy
Edit
ip_addresses = [
    "142.250.193.14",
    "8.8.8.8",
    "1.1.1.1",
    "172.217.194.190"
]
