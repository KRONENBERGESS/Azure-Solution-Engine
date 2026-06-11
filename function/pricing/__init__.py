import logging
import json
import requests
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        url = (
            "https://prices.azure.com/api/retail/prices"
            "?$filter=serviceName eq 'Virtual Machines' "
            "and armRegionName eq 'uaenorth'"
        )

        response = requests.get(url, timeout=20)
        response.raise_for_status()
        data = response.json()

        return func.HttpResponse(
            body=json.dumps({
                "retailPrice": data["Items"][0]["retailPrice"]
            }),
            status_code=200,
            headers={
                "Content-Type": "application/json"
            }
        )

    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse(
            body=json.dumps({
                "retailPrice": 0.096,
                "note": "fallback"
            }),
            status_code=200,
            headers={
                "Content-Type": "application/json"
            }
        )