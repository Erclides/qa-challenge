import requests

class APIClient:
    """
    Client para interagir com a API do desafio.
    Suporta autenticação JWT e CRUD de usuários/posts.
    """
    def __init__(self, base_url, username=None, password=None):
        self.base_url = base_url.rstrip("/")
        self.token = None
        if username and password:
            self.authenticate(username, password)

    def authenticate(self, username: str, password: str):
        """
        Gera JWT via endpoint /token e guarda no header Authorization.
        """
        status, data = self.post("/token", {"username": username, "password": password}, include_token=False)
        if status == 200 and "access_token" in data:
            self.token = data["access_token"]
        else:
            raise Exception(f"Falha ao autenticar: {status}, {data}")

    def _request(self, method, endpoint, payload=None, include_token=True):
        """
        Request genérico com timeout, tratamento de JSON e headers JWT.
        """
        url = f"{self.base_url}{endpoint}"
        headers = {}

        if include_token and self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        try:
            response = requests.request(
                method=method,
                url=url,
                json=payload,
                headers=headers,
                timeout=10
            )

            try:
                data = response.json()
            except ValueError:
                data = None

            return response.status_code, data

        except requests.exceptions.RequestException as e:
            return 500, {"error": str(e)}

    # ---------------- Métodos CRUD -----------------------

    def get(self, endpoint):
        return self._request("GET", endpoint)

    def post(self, endpoint, payload, include_token=True):
        return self._request("POST", endpoint, payload, include_token)

    def put(self, endpoint, payload):
        return self._request("PUT", endpoint, payload)

    def patch(self, endpoint, payload):
        return self._request("PATCH", endpoint, payload)

    def delete(self, endpoint):
        return self._request("DELETE", endpoint)
