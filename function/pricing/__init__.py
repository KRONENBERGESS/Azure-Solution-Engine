import requests
import logging
import  azure.functions as func

def main(req):
    try:
        url = (
            "https://prices.azure.com/api/retail/prices"
            "?$filter=serviceName eq 'Virtual Machines' "
            "and armRegionName eq 'uaenorth'"
        )

        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()
        first_item = data["Items"][0]

        return {
            "status": 200,
            "body": first_item
        }

    except Exception as e:
        logging.error(str(e))
        return {
            "status": 200,
            "body": {
                "retailPrice": 0.096,
                "note": "Fallback pricing (Azure Retail Prices API unavailable)"
            }
        }