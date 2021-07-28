############------------ IMPORTS ------------############
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

############------------ GLOBAL VARIABLE(S) ------------############
dataset = 'rohanrao/formula-1-world-championship-1950-2020'
path = 'rohanrao/formula-1-world-championship-1950-2020?select=constructors.csv'

############------------ FUNCTION(S) ------------############
def import_data():
    
    api = KaggleApi()
    api.authenticate()
    
    api.dataset_download_files(dataset, path)
    
    api.dataset_download_file(dataset, 'constructors.csv', path)
    api.dataset_download_file(dataset, 'constructors.sqlite', path)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    import_data()