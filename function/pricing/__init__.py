import json
import requests
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        service = req.params.get('service')
        region = req.params.get('region', 'uaenorth')
        sku = req.params.get('sku')
        unit = req.params.get('unit', 'month')
        os_type = req.params.get('os', 'linux')

        if not service or not sku:
            return func.HttpResponse(
                json.dumps({
                    "error": "Missing service or sku"
                }),
                status_code=400,
                mimetype="application/json"
            )

        if service.lower() != "vm":
            return func.HttpResponse(
                json.dumps({
                    "error": f"Service '{service}' not implemented yet"
                }),
                status_code=200,
                mimetype="application/json"
            )

        pricing_url = (
            "https://prices.azure.com/api/retail/prices"
            f"?$filter=serviceName eq 'Virtual Machines'"
            f" and armRegionName eq '{region}'"
            f" and armSkuName eq '{sku}'"
            f" and priceType eq 'Consumption'"
        )

        response = requests.get(pricing_url, timeout=15)
        response.raise_for_status()
        data = response.json()

        items = data.get("Items", [])

        # OS filtering after retrieval
        if os_type.lower() == "linux":
            items = [
                i for i in items
                if "windows" not in i.get("productName", "").lower()
            ]
        elif os_type.lower() == "windows":
            items = [
                i for i in items
                if "windows" in i.get("productName", "").lower()
            ]

        # Exclude Spot rows unless explicitly needed
        items = [
            i for i in items
            if "spot" not in i.get("meterName", "").lower()
        ]

        if not items:
            return func.HttpResponse(
                json.dumps({
                    "error": "No pricing found",
                    "service": service,
                    "sku": sku,
                    "region": region,
                    "os": os_type
                }),
                status_code=200,
                mimetype="application/json"
            )

        item = items[0]
        hourly_price = item["retailPrice"]
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

    except Exception as e:
        return func.HttpResponse(
            json.dumps({
                "error": "Function error",
                "details": str(e)
            }),
            status_code=500,
            mimetype="application/json"
        )