import pandas as pd
import numpy as np


def create_int_df(rows=100, cols=5):
    return pd.DataFrame(np.random.randint(0, 100, size=(rows, cols)), columns=[i for i in range(cols)])


def create_float_df(rows=100, cols=5):
    return pd.DataFrame(np.random.random((rows, cols)), columns=[i for i in range(cols)])


def create_tfidf_test_df():
    word_dict = {'allo': [1, 0, 3], 'jumanji': [0, 0, 1], 'bye': [1, 1, 1], 'poil': [0, 0, 0]}
    word_dict = {'the': [2, 1], 'car': [1, 0], 'truck': [0, 1], 'others': [4, 5]}
    return pd.DataFrame(word_dict)


def tfidf_df(df):
    return (df.div(df.sum(axis=1), axis=0))*np.log(len(df)/(df>0).sum())


if __name__ == '__main__':
    pd.set_option('display.width', 230)
    pd.set_option('display.max_columns', 15)
    pd.set_option('min_rows', 15)

    df = create_tfidf_test_df()
    tf = tfidf_df(df)
    print(df.div(df.sum(axis=1), axis=0))
    print(df)
    print(tf)
