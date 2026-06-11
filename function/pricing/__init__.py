import logging
import requests
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        url = (
            "https://prices.azure.com/api/retail/prices"
            "?$filter=serviceName eq 'Virtual Machines' "
            "and armRegionName eq 'uaenorth'"
        )

        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()

        return func.HttpResponse(
            body=str(data["Items"][0]),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse(
            body='{"retailPrice": 0.096, "note": "Fallback pricing"}',
            status_code=200,
            mimetype="application/json"
        )