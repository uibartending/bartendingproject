from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

homepage_images = [

]

recipe_data = [
    {
        "title": "",
        "description": "",
        "img": "",
        "items": [
    
        ],
        "steps": [
      
        ]
    },
    {
        "title": "",
        "description": "",
        "img": "",
        "items": [
    
        ],
        "steps": [
      
        ]
    },
    {
        "title": "",
        "description": "",
        "img": "",
        "items": [
    
        ],
        "steps": [
      
        ]
    }
]

quiz = [

]


@app.route('/')
def main():
    global learning_status

    return render_template('index.html', status=learning_status)


@app.route('/basics/<id>')
def basics(id):

    global learning_status
    global basic_material0
    global basic_material1
    print(id)

    if id=="0":
        return render_template('basic0.html', status=learning_status, data=basic_material0)
    else:
        return render_template('basic1.html', status=learning_status, data=basic_material1)


@app.route('/recipes/<id>')
def recipe(id):

    global recipe_data
    global learning_status
    id = int(id)

    return render_template('recipe.html', status=learning_status, data=recipe_data[int(id)], recipe_index=id)


@app.route('/quiz/<id>')
def quiz(id):

    global quiz
    global learning_status
    global basic_material0
    global quiz_answers

    id = int(id)



    return render_template('quiz.html', status=learning_status, quiz_index=id, data=basic_material0, answer=quiz_answers[id])



if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
