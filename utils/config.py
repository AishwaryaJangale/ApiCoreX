import os
from dotenv import load_dotenv

# Load default base URL or from environment
load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://reqres.in/api")
