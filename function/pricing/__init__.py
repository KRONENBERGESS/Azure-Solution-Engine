import json
import requests
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    service = req.params.get('service')
    region = req.params.get('region', 'uaenorth')
    sku = req.params.get('sku')
    unit = req.params.get('unit', 'hour')

    if not service or not sku:
        return func.HttpResponse(
            json.dumps({"error": "Missing service or sku"}),
            status_code=400,
            mimetype="application/json"
        )

    pricing_url = (
        "https://prices.azure.com/api/retail/prices"
        f"?$filter=armRegionName eq '{region}'"
        f" and skuName eq '{sku}'"
    )

    response = requests.get(pricing_url, timeout=10)
    data = response.json()

    if not data.get("Items"):
        return func.HttpResponse(
            json.dumps({"error": "No pricing found"}),
            status_code=404,
            mimetype="application/json"
        )

    hourly_price = data["Items"][0]["retailPrice"]

    monthly_price = hourly_price * 730 if unit == "month" else hourly_price

    return func.HttpResponse(
        json.dumps({
            "service": service,
            "sku": sku,
            "region": region,
            "hourlyPrice": hourly_price,
            "monthlyPrice": monthly_price
        }),
        status_code=200,
        mimetype="application/json"
    )