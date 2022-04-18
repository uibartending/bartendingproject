from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

homepage_images = [

]

data = [
    {
        "id":"0",
        "title":"margarita",
        "ingredients":[
            {
                "id":"0",
                "name":"Ice",
                "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png",
                "type":"ing"
            },
            {
                "id":"1",
                "name":"Tequila",
                "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png",
                "type":"ing"
            },
            {
                "id":"2",
                "name":"Lime",
                "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png",
                "type":"ing"
            },
            {
                "id":"3",
                "name":"Shaker",
                "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png",
                "type":"tool"
            },
            {
                "id":"4",
                "name":"Margarita Glass",
                "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png",
                "type":"tool"
            },
            {
                "id":"5",
                "name":"Measurements",
                "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png",
                "type":"tool"
            }
        ],
        "steps":[
            {
                "id":"0",
                "text":"Squeeze 1 oz. of lime juice. Measure out 1 oz. Cointreau. Measure out 2 oz. Tequila."
            },
            {
                "id":"1",
                "text":"Combine ingredients into shaker. Shake well to combine."
            },
            {
                "id":"2",
                "text":"Optional: Salt rims of margarita glass. Optional: Slice lime wedges to put on side. Pour drink into margarita glass + enjoy!"
            },
        ]
    },
    {
        "id":"1",
        "title":"cosmo",
        "ingredients":[
            {
                "id":"0",
                "name":"Ice",
                "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png",
                "type":"ing"
            },
            {
                "id":"1",
                "name":"Vodka",
                "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png",
                "type":"ing"
            },
            {
                "id":"2",
                "name":"Cranberry",
                "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png",
                "type":"ing"
            },
            {
                "id":"3",
                "name":"Cranberry",
                "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png",
                "type":"ing"
            },
            {
                "id":"2",
                "name":"cranberry",
                "img":"",
                "type":"tool"
            }
        ],
          "steps":[
            {
                "id":"1",
                "text":"Squeeze 1 oz. of lime juice. Measure out 1 oz. Cointreau. Measure out 2 oz. Tequila."
            },
            {
                "id":"2",
                "text":"Combine ingredients into shaker. Shake well to combine."
            },
            {
                "id":"3",
                "text":"Optional: Salt rims of margarita glass. Optional: Slice lime wedges to put on side. Pour drink into margarita glass + enjoy!"
            },
        ]
    },
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
    template = 'learn_'+str(kind)+'.html'
    to_display = data[0]
    for drink in data:
        if drink["id"]==str(id):
            to_display = drink
    materials=to_display["ingredients"]
    steps=to_display["steps"]
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
