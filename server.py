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
                "name":"ice",
                "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png",
            },
            {
                "id":"1",
                "name":"tequila",
                "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png",
            },
            {
                "id":"2",
                "name":"lime juice",
                "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png",
            },
            {
                "id":"3",
                "name":"cointreau",
                "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png",
            },
        ],
        "tools":[
            {
                "id":"0",
                "name":"shaker",
                "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png",
            },
            {
                "id":"1",
                "name":"glass",
                "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png",
            },
        ],
        "steps":[
            {
                "id":"0",
                "text":"Squeeze 1 oz. of lime juice<br>Measure out 1 oz. Cointreau<br>Measure out 2 oz. Tequila ",
                "tools":["Margarita Glass", "Measurements", "Shaker"],
                "ingredients":["Cointreau", "Lime Juice", "Tequila"],
                "img":["https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"]
            },
            {
                "id":"1",
                "text":"Combine ingredients into shaker<br>Shake well to combine",
                "tools":["shaker"],
                "ingredients":[""],
                "img":["https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"]
            },
            {
                "id":"2",
                "text":"Optional: Salt rims of margarita glass <br>Optional: Slice lime wedges to put on side<br>Pour drink into margarita glass + enjoy!",
                "tools":["Margarita Glass"],
                "ingredients":["Salt", "Fresh Lime"],
                "img":["https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"]
            },
        ],
    },
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
               "id":"1",
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
               "text":"Take 1 teaspoon of lime juice. Take 1 teaspoon of cranberry juice. Measure out 2 oz. vodka. Measure out 1/2 oz. triple sec.",
               "tools":["teaspoon", "measurements", "martini glass"],
               "ingredients":["lime juice", "cranberry juice", "vodka", "triple sec"],
               "img":["https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"]
           },
           {
               "id":"1",
               "text":"Combine ingredients into shaker. Shake well to combine.",
               "tools":["shaker"],
               "ingredients":[""],
               "img":["https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"]
           },
           {
               "id":"2",
               "text":"Optional: Garnish with orange peel. Optional: Peel the orange twist over the filled cocktail glass. Pour drink into martini glass + enjoy!",
               "tools":["martini glass"],
               "ingredients":["orange peel"],
               "img":["https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"]
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
               "id":"1",
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
               "text":"Take 5 teaspoons of coconut cream. Take 5 teaspoons of pineapple juice. Measure out 2 oz. light rum. Measure out 1/2 oz. lime juice.",
               "tools":["teaspoon", "measurements", "martini glass"],
               "ingredients":["coconut cream", "pineapple juice", "light rum", "lime juice"],
               "img":["https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"]
           },
           {
               "id":"1",
               "text":"Combine ingredients into shaker. Shake vigorously to combine.",
               "tools":["shaker"],
               "ingredients":[""],
               "img":["https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"]
           },
           {
               "id":"2",
               "text":"Optional: Garnish with a pineapple leaf. Optional: Garnish with a pineapple wedge. Pour drink into martini glass + enjoy!",
               "tools":["martini glass"],
               "ingredients":["pineapple leaf", "pineapple wedge"],
               "img":["https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"]
           },
       ]
},
]


quiz = [

]


@app.route('/')
def main():
    return render_template('home.html', data=data)


@app.route('/learn/<id>/<kind>/<page>')
def learn(id, kind, page):
    template = 'learn_'+str(kind)+'.html'
    to_display = data[0]
    for drink in data:
        if drink["id"]==str(id):
            to_display = drink
    materials=to_display["ingredients"]
    tools=to_display["tools"]
    steps=to_display["steps"]
    step=steps[0]
    for i in steps:
        if i["id"]==str(int(page)-1):
            step=i
    return(render_template(template, materials=materials, tools=tools, step=step, page=page))


@app.route('/quiz/<id>')
def quiz(id):
    return render_template('quiz_level2.html', data=data, id=id)



if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
