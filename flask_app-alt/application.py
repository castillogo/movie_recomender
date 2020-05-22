"""pip install -U Flask"""

from flask import Flask, render_template, request
from recommender import random_recommend

app = Flask(__name__)
#make this file the center of the app
#we launch this file from the terminal to start the app

@app.route('/') #whatever the function below is, route it to '/'
@app.route('/index')
def hello_world():
    return render_template('index.html') #templates/index.html

@app.route('/recommender')
def recommender():
    user_input = request.args
    result_list = random_recommend(8)
    return render_template('recommender.html',
                            result_html=result_list,
                            user_input= user_input)

if __name__ == '__main__':
    app.run(debug=True)
