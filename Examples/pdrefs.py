import pandas as pd
import numpy as np


### Utils pour creer dfs generiques ###

# Df filled with random ints 0-100, nb of rows and cols can be set with params. Row/Col labels: 0, 1, 2...
def create_int_df(rows=100, cols=5):
    return pd.DataFrame(np.random.randint(0, 100, size=(rows, cols)), columns=[i for i in range(cols)])


# Df filled with random floats 0-1, nb of rows and cols can be set with params. Row/Col labels: 0, 1, 2...
def create_float_df(rows=100, cols=5):
    return pd.DataFrame(np.random.random((rows, cols)), columns=[i for i in range(cols)])


def create_docterm_df():
    word_dict = {'allo': [1, 0, 3], 'jumanji': [0, 0, 1], 'bye': [1, 1, 1], 'poil': [0, 0, 0]}
    word_dict = {'the': [2, 1], 'car': [1, 0], 'truck': [0, 1], 'others': [4, 5]}
    return pd.DataFrame(word_dict)


### Refs ###
def common_operations(df=create_int_df()):
    df = create_int_df()
    print('Base DF')
    print(df)

    print('\n***\n')

    print('Multiplication')
    print(df*2)


def useful_df_tricks(df=create_int_df()):
    # Tricks and useful functions or shenanigans to work with dataframes

    # To copy a df to clipboard, can be pasted into excel/sheets/txt
    print('Copying df to clipboard via df.to_clipboard()')
    df.to_clipboard()


# calc tfidf, docterm df (rows are docs and columns are words; cells are word occs per doc)
def tfidf_df(df):
    return (df.div(df.sum(axis=1), axis=0))*np.log(len(df)/(df>0).sum())


if __name__ == '__main__':
    pd.set_option('display.width', 230)
    pd.set_option('display.max_columns', 15)
    pd.set_option('min_rows', 15)

    common_operations()
    #useful_df_tricks()

