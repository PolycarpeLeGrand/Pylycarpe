import pickle
from pathlib import Path


def pathlib_demo():
    print('Starting pathlib demo!')

    # Creating Path object at curr directory
    curr_path = Path.cwd()
    print(f'Path from Path.cwd(). File path: {curr_path} - Var type: {type(curr_path)}')

    # Creating Path object from string
    other_path = Path('C:/')

a = Path('.')
#print(a.cwd().rglob(f'*.py'))
pathlib_demo()

# gerer path pathlib
# os
# pickle
# input
# txt i/o
# csv
