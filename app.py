import flask
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os, requests, apiCalls



app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    # todo figure out how to do one api call for these images
    # breakfast = apiCalls.api()
    # lunch = apiCalls.lunch()
    # dinner = apiCalls.dinner()
    # images = []
    # for i in range(1, 3):
    #     images.append(breakfast['hits'][i]['recipe']['image'])
    #     images.append(lunch['hits'][i]['recipe']['image'])
    #     images.append(dinner['hits'][i]['recipe']['image'])
    # Automatically set these images from the api, we cannot do too many api calls at once so I had to manually enter these images)
    return render_template('index.html', image1= "https://www.edamam.com/web-img/e26/e267487d5cd69a038c3284931b4a3c1b.jpg",
                           image2= "https://www.edamam.com/web-img/ea3/ea3d4f71561834c9ba83a4f94855c1a0.jpg",
                           image3 = "https://www.edamam.com/web-img/b41/b4132f24268a9faeb8eb84bc164f39c1.jpg",
                           image4= "https://www.edamam.com/web-img/54d/54d01bbcb5537f018e723982af112c57.jpg",
                           image5="https://www.edamam.com/web-img/81f/81f405106c1d3a69232c98fba2f05565.jpg",
                           image6= "https://www.edamam.com/web-img/fb0/fb08a81382ac836ec709fee50d0f5123.jpeg")



@app.route('/recipes', methods=['POST'])  # , methods=['POST'])    -- **Waiting for questionnaire response**
# The API_Calls are shooting me with an error. Please advise on the modules that need to be installed to make it work properly.
def recipes():
    response = apiCalls.api()
    print(flask.request.form)
    return render_template("response.html", response=response['hits'][0]['recipe']['url'])


@app.route('/quiz')
def questions():
    q1 = "Are you on a diet? If so which one"
    q2 = "Would you like recipes to be free of anything?"
    q3 = "How would you like your diet?"
    q4 = "What is your maximum calorie intake?"
    return flask.render_template(
        "quiz.html",
        question1=q1,
        question2=q2,
        question3=q3,
        question4=q4
    )
@app.route('/answers', methods=['POST'])
def user_answers():
    value = requests.questions['value']
    return value





app.run(
    port=int(os.getenv('PORT', 8086)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)

if __name__ == '__main__':
    app.run(debug=True)
