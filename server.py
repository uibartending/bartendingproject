from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

homepage_images = [

]

material_1 = [
    {
        id: 0,
        "title": "",
        "type": "",
        "img": ""
    },
    {
        id: 1,
        "title": "",
        "type": "",
        "img": ""
    },
    {
        id: 2,
        "title": "",
        "type": "",
        "img": ""
    },
    {
        id: 3,
        "title": "",
        "type": "",
        "img": ""
    }
]


steps_1 = [
    {
        id: 0,
        "title": "",
        "description": ""
    },
    {
        id: 1,
        "title": "",
        "description": ""
    },
    {
        id: 2,
        "title": "",
        "description": ""
    },
    {
        id: 3,
        "title": "",
        "description": ""
    }
]

material_2 = [
    {
        id: 0,
        "title": "",
        "img": ""
    },
    {
        id: 1,
        "title": "",
        "img": ""
    },
    {
        id: 2,
        "title": "",
        "img": ""
    },
    {
        id: 3,
        "title": "",
        "img": ""
    }
]

steps_2 = [
    {
        id: 0,
        "title": "",
        "type": "",
        "description": ""
    },
    {
        id: 1,
        "title": "",
        "type": "",
        "description": ""
    },
    {
        id: 2,
        "title": "",
 
        "description": ""
    },
    {
        id: 3,
        "title": "",
        "description": ""
    }
]

material_3 = [
    {
        id: 0,
        "title": "",
        "type": "",
        "img": ""
    },
    {
        id: 1,
        "title": "",
        "img": ""
    },
    {
        id: 2,
        "title": "",
        "img": ""
    },
    {
        id: 3,
        "title": "",
        "img": ""
    }
]

steps_3 = [
    {
        id: 0,
        "title": "",
        "description": ""
    },
    {
        id: 1,
        "title": "",
        "description": ""
    },
    {
        id: 2,
        "title": "",
        "description": ""
    },
    {
        id: 3,
        "title": "",
        "description": ""
    }
]

quiz = [

]


@app.route('/')
def main():
    return render_template('home.html')


@app.route('/learn/<id>/<kind>/<page>')
def learn(id, kind, page):
    template = 'learn_'+kind+'.html'
    materials = 'material_'+id
    steps = 'step_'+id
    return(render_template(template, materials=materials, steps=steps, page=page))


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
