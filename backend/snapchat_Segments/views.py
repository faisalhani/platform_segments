# snapchat_Segments/views.py

from django.http import JsonResponse
from .models import CustomerList
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import redirect
from django.conf import settings
import requests

def customer_list_list(request):
    # Logic to retrieve and return a list of customer lists
    customer_lists = CustomerList.objects.all()
    data = {'customer_lists': list(customer_lists.values())}
    return JsonResponse(data)

def customer_list_detail(request, pk):
    # Logic to retrieve and return a specific customer list
    try:
        customer_list = CustomerList.objects.get(pk=pk)
        data = {'customer_list': model_to_dict(customer_list)}
        return JsonResponse(data)
    except CustomerList.DoesNotExist:
        return JsonResponse({'error': 'Customer list does not exist'}, status=404)

def start_oauth(request):
    # Construct the authorization URL with required parameters
    authorization_url = 'https://accounts.snapchat.com/login/oauth2/authorize'
    params = {
        'client_id': settings.SNAPCHAT_CLIENT_ID,  # Your Snapchat app client ID
        'redirect_uri': settings.SNAPCHAT_REDIRECT_URI,  # Your redirect URI
        'response_type': 'code',
        'scope': 'snapchat-marketing-api',  # Scope for accessing Snapchat Marketing API
    }
    # Construct the full URL
    redirect_url = f"{authorization_url}?{'&'.join([f'{key}={value}' for key, value in params.items()])}"
    
    # Redirect the user to the authorization URL
    return redirect(redirect_url)

# https://127.0.0.1:8000/callback?code=ylIOBo68kZaCRm8nweZecbLC0g-FPLZVFPr1fNptjOs
class SnapchatCallbackView(View):
     def get(self, request):
        # Extract the authorization code from the URL query parameters
        code = request.GET.get('code')

        if code:
            # Construct the payload for token generation
            payload = {
                'grant_type': 'authorization_code',
                'client_id': settings.SNAPCHAT_CLIENT_ID,  # Your Snapchat app client ID
                'client_secret': settings.SNAPCHAT_CLIENT_SECRET,  # Your Snapchat app client secret
                'code': code,
                'redirect_uri': settings.SNAPCHAT_REDIRECT_URI,  # Your redirect URI
            }

            # Make a POST request to exchange the authorization code for an access token
            response = requests.post('https://accounts.snapchat.com/login/oauth2/access_token', data=payload)

            if response.status_code == 200:
                # Token generation successful
                data = response.json()
                access_token = data.get('access_token')
                refresh_token = data.get('refresh_token')
                # Now you can store the access_token and refresh_token in your database or session
                return HttpResponse("Access token obtained successfully")
            else:
                # Token generation failed
                return HttpResponse("Failed to obtain access token")

        else:
            # Authorization code not found in the URL
            return HttpResponse("Authorization code not found")