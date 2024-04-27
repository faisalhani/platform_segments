from api import get_authorization_url, exchange_code_for_token, make_api_request
import webbrowser
from urllib.parse import urlparse, parse_qs

def test_snapchat_api_integration():
    # Get Authorization URL
    auth_url = get_authorization_url()
    print("Authorization URL:", auth_url)

    # Open web browser to navigate to Authorization URL
    webbrowser.open(auth_url)

    # Wait for user to complete authorization and return back to the Redirect URI
    redirect_uri_with_code = input("Enter the URL redirected back after authorization: ")

    # Parse the URL to extract the authorization code
    parsed_url = urlparse(redirect_uri_with_code)
    query_params = parse_qs(parsed_url.query)
    authorization_code = query_params.get('code', [''])[0]

    if authorization_code:
        print("Authorization Code obtained successfully:", authorization_code)

        # Exchange authorization code for access token
        access_token = exchange_code_for_token(authorization_code)
        if access_token:
            print("Access Token obtained successfully:", access_token)

            # Make API request using the access token
            api_response = make_api_request(access_token)
            if api_response:
                print("API Response:", api_response)
            else:
                print("Failed to make API request.")
        else:
            print("Failed to obtain access token.")
    else:
        print("Authorization code not found in the URL.")


# Call the function to test the Snapchat API integration
test_snapchat_api_integration()