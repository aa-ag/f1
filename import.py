############------------ IMPORTS ------------############
import json
# import kaggle
# from kaggle.api.kaggle_api_extended import KaggleApi


############------------ GLOBAL VARIABLE(S) ------------############
dataset = 'uciml/iris'
path = 'datasets/iris'

f = open('kaggle.json', 'r')
data = json.load(f)

username = data['username']
key = data['key']

print(username, key)