from flask import Flask, render_template, request
from recommender import random_recommend
import pandas as pd
import numpy as np
from sklearn.decomposition import NMF
import pandas as pd
import random


app = Flask(__name__)
#make this file the center of the app
#we launch this file from the terminal to start the app

@app.route('/') #whatever the function below is, route it to '/'
@app.route('/index')
def hello_world():
    return render_template('index.html') #templates/index.html

@app.route('/recommender')
def recommender():
    #by default, request.args is an ImmutableMultiDict
    #where keys --> names from HTML form, and vals ---> user input
    user_input = dict(request.args)
    user_input_movies = list(user_input.values())[::2]
    user_input_ratings = list(user_input.values())[1::2]
    user_input_movies2=[]

    """YOUR TASK:"""


    #Write a python function (or multiple) that does the following:
        # 1. Take in user input from the HTML form (dictionary)
        # 2. Map the movies to the database / dataframe
        # 3. Convert the input into a New User Array (601st), with length of ~9000
        # 4. Then use the components of the pre-trained NMF to transform this array (predict)
        # 5. Map the resulting movie "recommendations" to real names.
        # 6. Return the names (e.g. list)


    MOVIES = [x[:-7] for x in (pd.read_csv('movies.csv'))['title'].values.tolist()]


    #check =  all(item in user_input_movies for item in MOVIES)
    #[True if x in MOVIES else False for x in user_input_movies]
    userprintout = [x if x in MOVIES else 'sorry: This movie does not exist' for x in user_input_movies]
    user_input2 = zip(userprintout, user_input_ratings)
    result_list = random_recommend(user_input_movies, user_input_ratings)

#    if check==True:
#    elif check==False:
#        user_input2 = dictionary

#        yield user_input2



    return render_template('recommender.html', result_html=result_list, user_input_html = user_input2)

### Dynamic URLS in Flask!
# @app.route('/<name>')
# def greet(name):
#     if name == 'paul':
#         return f"Hello, {name}. Now training using NMF!"
#     else:
#         return "This isn't Paul. No training allowed."
if __name__ == '__main__':
    app.run(debug=True)
