import requests

url = 'https://api.lulu.com/print-job-cost-calculations/'

payload = """
{
    "line_items": [
        {
            "page_count": 32,
            "pod_package_id": "0600X0900BWSTDPB060UW444MXX",
            "quantity": 20
        },
        {
            "page_count": 324,
            "pod_package_id": "0425X0687BWSTDLW060UC444GRB",
            "quantity": 200
        }
    ],
    "shipping_address": {
        "city": "Washington",
        "country_code": "US",
        "postcode": "20540",
        "state_code": "DC",
        "street1": "101 Independence Ave SE"
    },
    "shipping_level": "EXPRESS"
}
"""

headers = { 
    'Content-Type': 'application/json',
    'Cache-Control': 'no-cache',
    'Authorization': 'Check Authentication menu', 
}

response = requests.request('POST', url, data=payload, headers=headers)

print(response.text)