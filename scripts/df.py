############------------ IMPORTS ------------############
import pandas as pd
import settings

############------------ GLOBAL VARIABLE(S) ------------############
constructors_df = pd.read_csv(settings.path_to_csv)


############------------ FUNCTION(S) ------------############
def print_df():
    print(constructors_df.head(1))
    # print(constructors)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    print_df()

    '''
    constructorId constructorRef     name nationality                                   url
0              1        mclaren  McLaren     British  http://en.wikipedia.org/wiki/McLaren
    '''