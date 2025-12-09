# core/utils.py
import json

def pretty_print_response(response):
    try:
        data = response.json()
    except Exception:
        print("Resposta não JSON:")
        print(response.text)
        return
    print(json.dumps(data, indent=2, ensure_ascii=False))
