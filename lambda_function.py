import os
import json
import requests

def lambda_handler(event, context):
    api_key = os.getenv("OPENROUTER_API_KEY")
    
    # Get prompt from event body
    try:
        body = json.loads(event.get("body", "{}"))
        prompt = body.get("prompt", "Hello from Lambda!")
    except json.JSONDecodeError:
        prompt = "Hello from Lambda!"

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek/deepseek-r1:free",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        if "choices" in result and len(result["choices"]) > 0:
            message = result["choices"][0]["message"]["content"]
        else:
            message = result.get("error", {}).get("message", str(result))

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"  # for browser CORS
            },
            "body": json.dumps({"response": message})
        }

    except requests.exceptions.RequestException as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }