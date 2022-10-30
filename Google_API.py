import os
from flask import Flask, render_template
import googleapiclient.discovery
from google.oauth2 import service_account



def get_credentials():
    scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
    GOOGLE_PRIVATE_KEY = 'JSON_KEY'

    account_info = {
      "private_key": GOOGLE_PRIVATE_KEY,
      "client_email": "KEY_gserviceaccount.com",
      "token_uri": "https://accounts.google.com/o/oauth2/token",
    }

    credentials = service_account.Credentials.from_service_account_info(account_info, scopes=scopes)
    return credentials


def get_service(service_name='sheets', api_version='v4'):
    credentials = get_credentials()
    service = googleapiclient.discovery.build(service_name, api_version, credentials=credentials)
    return service


app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    service = get_service()
    spreadsheet_id = ""
    range_name = ""

    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])

    return render_template('index.html', values=values)
    
if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)