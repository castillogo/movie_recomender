"""Write a python module (e.g. function) that returns movies randomly"""


import random

MOVIES = ['Shawshank Redemption',
          'Wizard of Oz',
          'Pulp Fiction',
          'Kill Bill',
          'Rings, The Lord of (2002)',
          'RegEx: The Movie',
          'FuzzyWuzzy Bubbly Buddy',
          'Docker: Unleashed',
          'Docker: FML',
          'Flask Fun',
          'Django Girls Unchained']

def random_recommend(num):
    result = random.choices(MOVIES, k=num)
    return result


"""GOAL: HAVE A SINGLE FUNCTION THAT RUNS THE ML PIPELINE:

For example:

def recommend_nmf():

    model = pickle.loads('nmf_model.bin')
    result = model.transform(user_input)

    return result

def main():
    result1 = func1()
    result2 = func2(result1)
    result3 = func3(result2)
    return result3
"""

if __name__ == '__main__':
    result = random_recommend(3)
    print(result)
