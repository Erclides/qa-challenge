
import os

BASE_URL = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
BROWSER = os.getenv("BROWSER", "chromium")  # alternativa: "chrome" ou "firefox"
HEADLESS = os.getenv("HEADLESS", "false").lower() in ("1", "true", "yes")
