from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account
import config

SCOPES = [

'https://www.googleapis.com/auth/spreadsheets',

'https://www.googleapis.com/auth/drive'

]

credentials = service_account.Credentials.from_service_account_file('credentials.json', scopes=SCOPES)

spreadsheet_service = build('sheets', 'v4', credentials=credentials)

drive_service = build('drive', 'v3', credentials=credentials)

def read_range(range_name):
    result = spreadsheet_service.spreadsheets().values().get(spreadsheetId=config.spreadsheet_id, range=range_name).execute()
    rows = result.get('values', [])
    return rows

def write_range(range_name,values):

    value_input_option = 'USER_ENTERED'

    body = { 'values': values}
    result = spreadsheet_service.spreadsheets().values().update(spreadsheetId=config.spreadsheet_id, range=range_name,valueInputOption=value_input_option, body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))
def add_data(login,time,text):
    rows = len(read_range(config.DataRange))
    write_range(f"Лист1!A{rows+1}:C",[[login,text,time]])