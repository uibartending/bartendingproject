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
       "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png",
        "ingredients":[
            {
                "id":"0",
                "name":"ice",
                "amt":"1",
                "unit":"oz",
                "img":"https://media.istockphoto.com/photos/ice-cubes-picture-id177131518?k=20&m=177131518&s=612x612&w=0&h=Bym7fbnY-eOI0CvFJhPJv_B4uLhTjul4ThN05p_Eao0=",
            },
            {
                "id":"1",
                "name":"tequila",
                 "amt":"2",
                "unit":"oz",
                "img":"https://www.patrontequila.com/binaries/mediumretina/content/gallery/patrontequila/products/patron-silver/bottle.png",
            },
            {
                "id":"2",
                "name":"lime juice",
                 "amt":"1",
                "unit":"oz",
                "img":"https://images.absolutdrinks.com/ingredient-images/Raw/Absolut/c9b31b0d-ed32-4125-b0e0-430e861d015f.jpg?imwidth=500",
            },
            {
                "id":"3",
                "name":"cointreau",
                "amt":"1",
                "unit":"oz",
                "img":"https://cdn.shopify.com/s/files/1/1569/9643/products/cointreau-triple-sec-orange-liqueur_1200x1200.jpg?v=1588276743",
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
        "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png",
       "ingredients":[
           {
               "id":"0",
               "name":"Ice",
                "amt":"1",
                "unit":"oz",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"1",
               "name":"vodka",
                  "amt":"2",
                "unit":"oz",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"2",
               "name":"Triple sec",
                  "amt":".5",
                "unit":"oz",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"3",
               "name":"Cranberry juice",
                  "amt":"1",
                "unit":"tsp",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"4",
               "name":"Lime juice",
                  "amt":"1",
                "unit":"tsp",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"5",
               "name":"Orange peel",
                  "amt":"1",
                "unit":"peel",
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
       "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png",
       "ingredients":[
           {
               "id":"0",
               "name":"Ice",
               "amt":"1",
               "unit":"oz",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"1",
               "name":"Light rum",
               "amt":"2",
               "unit":"oz",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"2",
               "name":"Coconut cream",
               "amt":"5",
               "unit":"tsp",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"3",
               "name":"Pineapple juice",
               "amt":"5",
               "unit":"tsp",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"4",
               "name":"Lime juice",
               "amt":".5",
               "unit":"oz",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"5",
               "name":"Pineapple wedge",
               "amt":"1",
               "unit":"wedge",
               "img":"https://www.webfx.com/wp-content/uploads/2021/10/generic-image-placeholder.png"
           },
           {
               "id":"6",
               "name":"Pineapple leaf",
               "amt":"1",
               "unit":"leaf",
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
userErrors={}
quiz = [

]
ingredientsTotal=[
 ]
@app.route('/ingredients', methods=['GET', 'POST'])
def getname():
    global data
    global ingredientsTotal
    json_data = request.get_json() 
    idnum = json_data["id"]
    ingrCorrect = [] 
    ingobj = data[idnum]["ingredients"]
    for ing in data[idnum]["ingredients"]:
        ingrCorrect.append(ing["name"])
    for  drink in data:
        for  ing in drink["ingredients"]:
            if ing["name"] not in ingredientsTotal:
                ingredientsTotal.append(ing["name"])
    length = len(data)
    return jsonify(ingredients = ingredientsTotal, ingredientsCorrect = ingrCorrect, drink = data[idnum],  length=length)

@app.route('/posterrors', methods=['GET', 'POST'])
def posterrors():
    global userErrors
    global data
    global ingredientsTotal
    json_data = request.get_json()
    er = json_data["errors"]
    user = json_data["user"]
    if not userErrors[user] :
        userErrors[user] = er + userErrors[user]      
    return jsonify(res = "YES")

@app.route('/')
def main():
    return render_template('home.html', data=data)

@app.route('/end')
def end():
       return render_template('endpage.html')

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
    return(render_template(template, materials=materials, tools=tools, step=step, page=page, id=id))


@app.route('/quiz/<quiznum>/<id>')
def quiz(id, quiznum):
    temp = int(id)
    template = 'quiz_level'+str(quiznum)+'.html'
    global data 
       
    return render_template(template, data=data, id=temp)


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
