from dotenv import load_dotenv
import requests
import os

load_dotenv()
secret_key = os.getenv('SECRET_KEY')

