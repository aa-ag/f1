############------------ IMPORTS ------------############
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

############------------ GLOBAL VARIABLE(S) ------------############
dataset = 'uciml/iris'
path = 'datasets/iris'

############------------ FUNCTION(S) ------------############
def import_data():
    
    api = KaggleApi()
    api.authenticate()
    
    api.dataset_download_files(dataset, path)
    
    api.dataset_download_file(dataset, 'Iris.csv', path)
    api.dataset_download_file(dataset, 'database.sqlite', path)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    import_data()