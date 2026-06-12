import json
import requests
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    service = req.params.get('service', 'vm')
    region = req.params.get('region', 'uaenorth')
    tier = req.params.get('tier', 'small')
    os = req.params.get('os', 'linux')

    # Map tier → SKU (example mapping)
    sku_map = {
        "small": "Standard_D2s_v5",
        "medium": "Standard_D4s_v5",
        "large": "Standard_D8s_v5"
    }

    sku = sku_map.get(tier, "Standard_D2s_v5")

    pricing_url = (
        "https://prices.azure.com/api/retail/prices"
        f"?$filter=serviceName eq 'Virtual Machines'"
        f" and armRegionName eq '{region}'"
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

    price = data["Items"][0]["retailPrice"]

    return func.HttpResponse(
        json.dumps({
            "sku": sku,
            "region": region,
            "retailPrice": price
        }),
        status_code=200,
        mimetype="application/json"
    )