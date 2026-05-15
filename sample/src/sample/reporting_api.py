import requests

def run():

    username = "sa_5cF4G8Fu"
    password = "3AxuG6CJuh9k902KC1LILTK2wH1AsUTP"

    base_url = "https://talentship.dev.octonomy.ai/api/appconnect/reporting/"
    tenant_id = "talentship"

    url = f"{base_url}agent"

    payload = {
        "tenant_id": tenant_id
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers,
        auth=(username, password)
    )

    print("Status Code:", response.status_code)
    print("Response:", response.text)


if __name__ == "__main__":
    run()