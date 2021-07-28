############------------ IMPORTS ------------############
import pandas as pd
import settings

############------------ GLOBAL VARIABLE(S) ------------############
constructors = pd.read_csv(settings.path_to_csv)


############------------ FUNCTION(S) ------------############
def print_df():
    print(constructors)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    print_df()