from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

homepage_images = [

]

data = [
{
       "id":"1",
       "title":"cosmo",
       "ingredients":[
           {
               "id":"0",
               "name":"Ice",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"1",
               "name":"Tequila",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"2",
               "name":"Triple sec",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"3",
               "name":"Cranberry juice",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"4",
               "name":"Lime juice",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"5",
               "name":"Orange peel",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           }
       ],
       "tools": [
           {
               "id":"0",
               "name":"Shaker",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"0",
               "name":"Martini glass",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"2",
               "name":"Measurements",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"3",
               "name":"Teaspoon",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           }
       ],
       "steps":[
           {
               "id":"0",
               "text":"Take 1 teaspoon of lime juice. Take 1 teaspoon of cranberry juice. Measure out 2 oz. vodka. Measure out 1/2 oz. triple sec."
           },
           {
               "id":"1",
               "text":"Combine ingredients into shaker. Shake well to combine."
           },
           {
               "id":"2",
               "text":"Optional: Garnish with orange peel. Optional: Peel the orange twist over the filled cocktail glass. Pour drink into martini glass + enjoy!"
           },
       ]
    },

    {
       "id":"2",
       "title": "Piña Colada",
       "ingredients":[
           {
               "id":"0",
               "name":"Ice",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"1",
               "name":"Light rum",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"2",
               "name":"Coconut cream",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"3",
               "name":"Pineapple juice",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"4",
               "name":"Lime juice",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"5",
               "name":"Pineapple wedge",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"6",
               "name":"Pineapple leaf",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           }
       ],
       "tools": [
           {
               "id":"0",
               "name":"Shaker",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"0",
               "name":"Martini glass",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"2",
               "name":"Measurements",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"3",
               "name":"Teaspoon",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           }
       ],
       "steps":[
           {
               "id":"0",
               "text":"Take 5 teaspoons of coconut cream. Take 5 teaspoons of pineapple juice. Measure out 2 oz. light rum. Measure out 1/2 oz. lime juice."
           },
           {
               "id":"1",
               "text":"Combine ingredients into shaker. Shake vigorously to combine."
           },
           {
               "id":"2",
               "text":"Optional: Garnish with a pineapple leaf. Optional: Garnish with a pineapple wedge. Pour drink into martini glass + enjoy!"
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
