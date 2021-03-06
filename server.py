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
        "title":"Margarita",
       "img":"https://www.patrontequila.com/binaries/content/gallery/patrontequila/recipes/patron-silver/patron-classic-margarita/hero_640x650_patron-classic-margarita.jpg",
        "ingredients":[
            {
                "id":"0",
                "name":"ice",
                "amt":"1",
                "unit":"oz",
                "img":"https://food.fnr.sndimg.com/content/dam/images/food/fullset/2014/10/15/0/fnd_Ice-Cubes-thinkstock.jpg.rend.hgtvcom.616.462.suffix/1413404558868.jpeg",
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
                "img":"https://www.thespruceeats.com/thmb/KIDItEQSR7SYGeYR5k9ExRJFpjE=/1333x1000/smart/filters:no_upscale()/thai-limeade-recipe-3217359-hero-02-91dbbaac0ec349e4b8f640aee05d18d1.jpg",
            },
            {
                "id":"3",
                "name":"cointreau",
                "amt":"1",
                "unit":"oz",
                "img":"https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Coinreau_original_v4.jpg/440px-Coinreau_original_v4.jpg",
            },
            {
                "id":"4",
                "name":"salt",
                "amt":"1",
                "unit":"oz",
                "img":"https://assets.katomcdn.com/q_auto,f_auto,w_500,dpr_2/products/229/229-C13212/229-c13212.jpg",
            },
        ],
        "tools":[
            {
                "id":"0",
                "name":"shaker",
                "img":"https://secure.img1-fg.wfcdn.com/im/50692895/resize-h755-w755%5Ecompr-r85/1219/121923770/24+Oz+Cocktail+Shaker.jpg",
            },
            {
                "id":"1",
                "name":"glass",
                "img":"https://secure.img1-fg.wfcdn.com/im/94706934/resize-h445%5Ecompr-r85/3640/36408915/Ritwik+7+oz.+Martini+Glass.jpg",
            },
            {
                "id":"2",
                "name":"measurements",
                "img":"https://assets.leevalley.com/Size5/10028/EV103-measuring-glass-f-01-r.jpg",
            },
        ],
        "steps":[
            {
                "id":"0",
                "text":"Squeeze 1 oz. of lime juice<br>Measure out 1 oz. Cointreau<br>Measure out 2 oz. Tequila",
                "tools":["glass", "Measurements", "Shaker"],
                "ingredients":["Cointreau", "Lime Juice", "Tequila"],
                "img":["https://www.homemadefoodjunkie.com/wp-content/uploads/2020/06/measuring-1800-tequila.jpg"]
            },
            {
                "id":"1",
                "text":"Combine ingredients into shaker<br>Shake well to combine",
                "tools":["shaker"],
                "ingredients":[""],
                "img":["https://www.thespruceeats.com/thmb/IzZLkkRDki_A5OiTSecDbNnsgZY=/940x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/GettyImages-859603292-5a79ec08a9d4f90036247b1c.jpg"]
            },
            {
                "id":"2",
                "text":"Optional: Salt rims of margarita glass <br>Optional: Slice lime wedges to put on side<br>Pour drink into margarita glass + enjoy!",
                "tools":["Margarita Glass"],
                "ingredients":["Salt", "Fresh Lime"],
                "img":["https://bakingamoment.com/wp-content/uploads/2019/04/IMG_4056-margarita-ingredients.jpg"]
            },
        ],
        "description":"A margarita is a sweet, sour, and salty cocktail that is guaranteed to please a crowd! Many people enjoy these strong and refershing drinks paired with Mexican food, but after learning our recipe here you can make them for any occasion!",
    },
    {
       "id":"1",
       "title":"Cosmopolitan",
        "img":"https://images.immediate.co.uk/production/volatile/sites/30/2020/08/cosmopolitan-7a6874f.jpg?quality=90&webp=true&resize=440,400",
       "ingredients":[
           {
               "id":"0",
               "name":"ice",
                "amt":"1",
                "unit":"oz",
               "img":"https://food.fnr.sndimg.com/content/dam/images/food/fullset/2014/10/15/0/fnd_Ice-Cubes-thinkstock.jpg.rend.hgtvcom.616.462.suffix/1413404558868.jpeg"
           },
           {
               "id":"1",
               "name":"vodka",
                  "amt":"2",
                "unit":"oz",
               "img":"https://mediacore.kyuubi.it/anticaenotecagiulianelli/media/img/2020/8/8/164133-large-vodka-smirnoff-n-21-37-5-lt-1-et-rossa.jpg"
           },
           {
               "id":"2",
               "name":"Triple sec",
                  "amt":".5",
                "unit":"oz",
               "img":"https://static.specsonline.com/wp-content/uploads/2021/08/008835211856.jpg"
           },
           {
               "id":"3",
               "name":"Cranberry juice",
                  "amt":"1",
                "unit":"tsp",
               "img":"https://m.media-amazon.com/images/I/81ARHIFCZ6L._SY741_PIbundle-8,TopRight,0,0_SX556SY741SH20_.jpg"
           },
           {
               "id":"4",
               "name":"Lime juice",
                  "amt":"1",
                "unit":"tsp",
               "img":"https://www.thespruceeats.com/thmb/KIDItEQSR7SYGeYR5k9ExRJFpjE=/1333x1000/smart/filters:no_upscale()/thai-limeade-recipe-3217359-hero-02-91dbbaac0ec349e4b8f640aee05d18d1.jpg"
           },
           {
               "id":"5",
               "name":"Orange peel",
                  "amt":"1",
                "unit":"peel",
               "img":"https://homesteading.com/wp-content/uploads/2019/09/59-The-Magnificent-Orange-Peel-Clever-Homestead-Uses-for-Citrus-Peels-ss-1200x900.jpg"
           }
       ],
       "tools": [
           {
               "id":"0",
               "name":"Shaker",
               "img":"https://secure.img1-fg.wfcdn.com/im/50692895/resize-h755-w755%5Ecompr-r85/1219/121923770/24+Oz+Cocktail+Shaker.jpg"
           },
           {
               "id":"1",
               "name":"Martini glass",
               "img":"https://secure.img1-fg.wfcdn.com/im/94706934/resize-h445%5Ecompr-r85/3640/36408915/Ritwik+7+oz.+Martini+Glass.jpg"
           },
           {
               "id":"2",
               "name":"Measurements",
               "img":"https://assets.leevalley.com/Size5/10028/EV103-measuring-glass-f-01-r.jpg"
           },
           {
               "id":"3",
               "name":"Teaspoon",
               "img":"https://www.amara.com/static/uploads/images-2/products/huge/43116/albi-teaspoon-464510.jpg"
           }
       ],
       "steps":[
           {
               "id":"0",
               "text":"Take 1 teaspoon of lime juice. <br> Take 1 teaspoon of cranberry juice. <br> Measure out 2 oz. vodka. <br> Measure out 1/2 oz. triple sec.",
               "tools":["teaspoon", "measurements", "martini glass"],
               "ingredients":["lime juice", "cranberry juice", "vodka", "triple sec"],
               "img":["https://www.homemadefoodjunkie.com/wp-content/uploads/2020/06/measuring-1800-tequila.jpg"]
           },
           {
               "id":"1",
               "text":"Combine ingredients into shaker. <br> Shake well to combine.",
               "tools":["shaker"],
               "ingredients":[""],
               "img":["https://www.thespruceeats.com/thmb/IzZLkkRDki_A5OiTSecDbNnsgZY=/940x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/GettyImages-859603292-5a79ec08a9d4f90036247b1c.jpg"]
           },
           {
               "id":"2",
               "text":"Optional: Garnish with orange peel. <br> Optional: Peel the orange twist over the filled cocktail glass. <br> Pour drink into martini glass + enjoy!",
               "tools":["martini glass"],
               "ingredients":["orange peel"],
               "img":["https://www.jocooks.com/wp-content/uploads/2020/03/cosmopolitan-cocktail-1-3.jpg"]
           },
       ],
       "description":"A Cosmopolitan, cosmo for short, is a simple Martini-style drink consisting of vodka, triplesec, cranberry juice, and lime juice best known for being a favorite of the characters on 'Sex and the City'. Channel your inner Carrie Bradshaw and learn how to make her favorite drink here!",
    },

    {
       "id":"2",
       "title": "Pi??a Colada",
       "img":"https://www.everyday-delicious.com/wp-content/uploads/2019/07/pina-colada-everyday-delicious-799x1200.jpg",
       "ingredients":[
           {
               "id":"0",
               "name":"ice",
               "amt":"1",
               "unit":"oz",
               "img":"https://food.fnr.sndimg.com/content/dam/images/food/fullset/2014/10/15/0/fnd_Ice-Cubes-thinkstock.jpg.rend.hgtvcom.616.462.suffix/1413404558868.jpeg"
           },
           {
               "id":"1",
               "name":"Light rum",
               "amt":"2",
               "unit":"oz",
               "img":"https://static.specsonline.com/wp-content/uploads/2021/07/008048001530.jpg"
           },
           {
               "id":"2",
               "name":"Coconut cream",
               "amt":"5",
               "unit":"tsp",
               "img":"https://m.media-amazon.com/images/I/51sDy+ZNW1L.jpg"
           },
           {
               "id":"3",
               "name":"Pineapple juice",
               "amt":"5",
               "unit":"tsp",
               "img":"https://m.media-amazon.com/images/I/41gFf1GZCCL.jpg"
           },
           {
               "id":"4",
               "name":"Pineapple wedge",
               "amt":"1",
               "unit":"wedge",
               "img":"https://media01.stockfood.com/largepreviews/Mjg1OTUxNDQ=/00922424-Wedge-of-pineapple.jpg"
           },
           {
               "id":"5",
               "name":"Pineapple leaf",
               "amt":"1",
               "unit":"leaf",
               "img":"https://images.herzindagi.info/image/2021/Jan/Benefits-Of-Pineapple-Leaves.jpg"
           }
       ],
       "tools": [
           {
               "id":"0",
               "name":"Shaker",
               "img":"https://secure.img1-fg.wfcdn.com/im/50692895/resize-h755-w755%5Ecompr-r85/1219/121923770/24+Oz+Cocktail+Shaker.jpg"
           },
           {
               "id":"1",
               "name":"Martini glass",
               "img":"https://secure.img1-fg.wfcdn.com/im/94706934/resize-h445%5Ecompr-r85/3640/36408915/Ritwik+7+oz.+Martini+Glass.jpg"
           },
           {
               "id":"2",
               "name":"Measurements",
               "img":"https://assets.leevalley.com/Size5/10028/EV103-measuring-glass-f-01-r.jpg"
           },
           {
               "id":"3",
               "name":"Teaspoon",
               "img":"https://www.amara.com/static/uploads/images-2/products/huge/43116/albi-teaspoon-464510.jpg"
           }
       ],
       "steps":[
           {
               "id":"0",
               "text":"Take 5 teaspoons of coconut cream.<br> Take 5 teaspoons of pineapple juice.<br> Measure out 2 oz. light rum.",
               "tools":["teaspoon", "measurements", "martini glass"],
               "ingredients":["coconut cream", "pineapple juice", "light rum"],
               "img":["https://www.homemadefoodjunkie.com/wp-content/uploads/2020/06/measuring-1800-tequila.jpg"]
           },
           {
               "id":"1",
               "text":"Combine ingredients into shaker.<br> Shake vigorously to combine.",
               "tools":["shaker"],
               "ingredients":[""],
               "img":["https://www.thespruceeats.com/thmb/IzZLkkRDki_A5OiTSecDbNnsgZY=/940x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/GettyImages-859603292-5a79ec08a9d4f90036247b1c.jpg"]
           },
           {
               "id":"2",
               "text":"Optional: Garnish with a pineapple leaf.<br> Optional: Garnish with a pineapple wedge.<br> Pour drink into martini glass + enjoy!",
               "tools":["martini glass"],
               "ingredients":["pineapple leaf", "pineapple wedge"],
               "img":["https://farm2.staticflickr.com/1829/29461128088_45fcc94bb4_o.jpg"]
           },
       ],
       "description":"This sweet and refreshing summer cocktail will transport you to a tropical beach no matter where you drink it. Served blended or over ice, this coconut-pineapple combo just can't be beat! Learn how to make your new favorite drink below.",
},
]
userErrors={}
user_data = {}

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
    if not user in userErrors:
        userErrors[user] = er
    else:
        userErrors[user] = userErrors[user]+er
    return jsonify(res = "YES")

@app.route('/posttime', methods=['GET', 'POST'])
def posttime():
    json_data = request.get_json()
    time = json_data["entry time"]
    user = json_data["user"]
    if not user in user_data:
        user_data[user] = [time]
    else:
        user_data[user].append(time)
    return jsonify(user_data=user_data)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('home.html', data=data, user_data=user_data)


@app.route('/learn/<id>/<kind>/<page>')
def learn(id, kind, page):
    template = 'learn_'+str(kind)+'.html'
    to_display = data[0]
    for drink in data:
        if drink["id"]==str(id):
            to_display = drink
    materials=to_display["ingredients"]
    tools=to_display["tools"]
    title=to_display["title"]
    description=to_display["description"]
    steps=to_display["steps"]
    step=steps[0]
    for i in steps:
        if i["id"]==str(int(page)-1):
            step=i
    return(render_template(template, materials=materials, tools=tools, step=step, page=page, id=id, title=title, description=description))


@app.route('/quiz/<quiznum>/<id>')
def quiz(id, quiznum):
    temp = int(id)
    template = 'quiz_level'+str(quiznum)+'.html'
    global data

    return render_template(template, data=data, id=temp)

@app.route('/end')
def end():
    return render_template('endpage.html', data=data, user_data=user_data)

@app.route('/results')
def results():
    global userErrors
    global data
    print(userErrors)
    numWrong = len(userErrors["ChiltonL"])
    return render_template('results.html', data=data, numWrong=numWrong)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
