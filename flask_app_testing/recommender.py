"""Write a python module (e.g. function) that returns movies randomly"""


import numpy as np
from sklearn.decomposition import NMF
import pandas as pd
import random
import pickle

MOVIES = [x[:-7] for x in (pd.read_csv('movies.csv'))['title'].values.tolist()]




#MOVIES = ['Shawshank Redemption',
#          'Wizard of Oz',
#          'Pulp Fiction',
#          'Kill Bill',
#          'Rings, The Lord of (2002)',
#          'RegEx: The Movie',
#          'FuzzyWuzzy Bubbly Buddy',
#          'Docker: Unleashed',
#          'Docker: FML',
#          'Flask Fun',
#          'Django Girls Unchained']

#   Add userinput as parameter to this FUNCTION and give the funcion a user user_input
#   transform user input so that it is a list of 3 with length equal to number of columns
#   replace the columns that represent the user id with the values the user has given
#   give that resulting list to line 40 (P = model.transform(user_input2))
#   nR is going to be the new recommendation list
#   find top values in nR (np.argsort or np.argmax)
#   find the index (or movieId) of those columns
#   find the name for those movieIds (iloc) or pandas.columns


def random_recommend(user_input_movies, user_input_ratings):
    ratings = pd.read_csv('ratings.csv')
    movies = pd.read_csv('movies.csv')
    moviesIdlist=movies['movieId'].tolist()
    MOVIES = [x[:-7] for x in (pd.read_csv('movies.csv'))['title'].values.tolist()]
    MOVIEID = [x for x in (pd.read_csv('movies.csv'))['movieId'].values.tolist()]
    movies['title'] = MOVIES
    ratings2=ratings.set_index(['userId'])
    ratings3 = ratings.drop(['timestamp'], axis=1)
    newmoviesratings = pd.merge(ratings3, movies, on='movieId')
    newmoviesratings2=newmoviesratings[['userId','title','rating']]
#    newf = newmoviesratings2.set_index('userId')
    newf = ratings3.pivot(index='userId', columns='movieId')
    actualmovieIdslist=ratings3['movieId'].tolist()
    newmoviesIDlist = [x for x in moviesIdlist if x in actualmovieIdslist]
    newf2=newf.fillna(3.000000)
    R=newf2.values
    model = pickle.load(open('finalized_model.sav', 'rb'))
    Q = model.components_
    P = model.transform(R)
    nR = np.dot(P, Q)
    randomuser = user_input_movies #['Fargo', 'Toy Story', 'Memento'] ### This need to be modifyed!
    randomratings = user_input_ratings ### This need to be modifyed
    randomlist = [3]*len(newmoviesIDlist)
    for x in range(len(randomuser)):
        index=MOVIES.index(randomuser[x])
        ID=MOVIEID[index]
        indexb=newmoviesIDlist.index(ID)
        randomlist[indexb]=randomratings[x]
#        x=x+1
    ratings4 = ratings3.groupby('userId')
    maxValue = ratings3['userId'].max()
    newUserID=maxValue+1
    array3=np.array(randomlist)
    array3=array3.reshape(1,-1)
    #model.fit(array3)
    #model.transform(array3)
    newuserrow=[newUserID]+randomlist
    newf3=newuserrow.append(newf2)
    R2=R.tolist()
    R3 = R2 + [randomlist]
    R4=np.array(R3)
    #model.fit(R4)
    Q = model.components_
    P = model.transform(R4)
    nR = np.dot(P, Q)
    finalList=nR.tolist()
    totalratingsnewuser=finalList[-1]
    finalDf1 = pd.DataFrame(
        {'movieid': newmoviesIDlist,
        'ratingsnewuser': totalratingsnewuser
        })
    finalDf2 = pd.DataFrame(
        {'title': MOVIES,
        'movieid': MOVIEID,
        })
    finaldf4 = pd.merge(finalDf2, finalDf1, on='movieid')
    finaldf5=finaldf4.dropna()
    finaldf6=finaldf5.sort_values('ratingsnewuser', ascending=False)
    finalmovielist=finaldf6['title'].tolist()
    finalmovielist2 = [x for x in finalmovielist if x not in randomuser]
    finaloutputlist=finalmovielist2[:8]
    return finaloutputlist

#def random_recommend(num):
#    result = random.choices(MOVIES, k=num)
#    return result


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
    result = random_recommend(user_input_movies, user_input_ratings)
    print(result)
