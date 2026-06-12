import json
import requests
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        service = req.params.get('service')
        region = req.params.get('region', 'uaenorth')
        sku = req.params.get('sku')
        unit = req.params.get('unit', 'month')
        os = req.params.get('os')

        if not service or not sku:
            return func.HttpResponse(
                json.dumps({
                    "error": "Missing service or sku"
                }),
                status_code=400,
                mimetype="application/json"
            )

        # Base filter
        pricing_url = (
            "https://prices.azure.com/api/retail/prices"
            f"?$filter=armRegionName eq '{region}'"
        )

        response = requests.get(pricing_url, timeout=10)
        response.raise_for_status()
        data = response.json()

        items = data.get("Items", [])

        # Basic filtering logic
        filtered = [
            i for i in items
            if sku.lower() in i.get("skuName", "").lower()
        ]

        if service.lower() == "vm":
            filtered = [
                i for i in filtered
                if i.get("serviceName", "").lower() == "virtual machines"
            ]

            if os:
                if os.lower() == "linux":
                    filtered = [
                        i for i in filtered
                        if "windows" not in i.get("productName", "").lower()
                    ]
                elif os.lower() == "windows":
                    filtered = [
                        i for i in filtered
                        if "windows" in i.get("productName", "").lower()
                    ]

        if not filtered:
            return func.HttpResponse(
                json.dumps({
                    "error": "No pricing found",
                    "service": service,
                    "sku": sku,
                    "region": region
                }),
                status_code=200,
                mimetype="application/json"
            )

        hourly_price = filtered[0]["retailPrice"]
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