import os
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env')
load_dotenv(dotenv_path)

# Get Snapchat API credentials from environment variables
CLIENT_ID = os.getenv('SNAPCHAT_CLIENT_ID')
CLIENT_SECRET = os.getenv('SNAPCHAT_CLIENT_SECRET')
REDIRECT_URI = os.getenv('SNAPCHAT_REDIRECT_URI')

# Snapchat API endpoints
AUTH_URL = 'https://accounts.snapchat.com/login/oauth2/authorize'
ACCESS_TOKEN_URL = 'https://accounts.snapchat.com/login/oauth2/access_token'
API_ENDPOINT = 'https://adsapi.snapchat.com/v1/adaccounts/{ad_account_id}/segments'


def get_authorization_url():
    # Construct Authorization URL
    authorization_url = f"{AUTH_URL}?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=snapchat-marketing-api"
    return authorization_url


def exchange_code_for_token(code):
    # Exchange code for access token
    payload = {
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
        'redirect_uri': REDIRECT_URI
    }
    response = requests.post(ACCESS_TOKEN_URL, data=payload)

    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data['access_token']
        return access_token
    else:
        print("Failed to exchange code for token:", response.text)
        return None


def make_api_request(access_token):
    # Make API request using the access token
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(API_ENDPOINT, headers=headers)

    if response.status_code == 200:
        api_response = response.json()
        return api_response
    else:
        print("API Request failed:", response.text)
        return None

# dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env')
