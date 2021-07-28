############------------ IMPORTS ------------############
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import settings

############------------ GLOBAL VARIABLE(S) ------------############
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('sheets-321223-19ca8a0993d5.json', scope)

client = gspread.authorize(credentials)

sheet = client.open('Kaggle-to-Local-csv-to-Sheet')

local_path_to_csv_file = settings.path_to_csv

############------------ FUNCTION(S) ------------############
def upload_data_from_local_csv_to_google_sheets():
    '''
     reads/opens csv file from local path,
     and imports data from csv to already connected/auth'd
     sheets file via google drive's api's `import_csv` function
    '''
    csv_file = open(local_path_to_csv_file, 'r')

    upload_data = csv_file.read()

    client.import_csv(sheet.id, data=upload_data)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    upload_data_from_local_csv_to_google_sheets()

