var length=0
let ppc_members=[]
var ingredients = [
    "Phyllis",
    "Angela",
    "Dwight",
    "Oscar",
    "Creed",
    "Pam",
    "Jim",
    "Stanley",
    "Michael",
    "Kevin",
    "Kelly"
]
var drink = {}
var ingredientsCorrect = [
]
var errors = []
var id = 1
var drkId = 0
function postVa(){
    indx = window.location.href.lastIndexOf('/')
    temp =window.location.href.substring(indx+1,indx+2)
    drkId = parseInt(temp)
    console.log(drkId)
    let data_to_save = JSON.stringify({"id":drkId})
    $.ajax({
        type: "POST",
        url: window.location.origin+"/ingredients",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : data_to_save,
        success: function(result){
            ingredients  = result["ingredients"]
            ingredientsCorrect  = result["ingredientsCorrect"]
            length = result["length"]
            drink = result["drink"]
            console.log(ingredients)
            console.log(drink)
            makenames(ingredients, ppc_members)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

function checkQuiz2(){
    dr = drink["ingredients"]
    for (id in drink["ingredients"]){
        seel = "#"+id
        val = $(seel).val()

        drid = drink["ingredients"][id]["amt"]
        if (val  ==  drid){
            console.log("Right")
        }
        else{
            errors.push({"id" : drkId, "val":val})
            $(seel).val("Incorrect")
            console.log(errors)
        }
    }
    postErrors()
}
function postErrors(){
    let data_to_save = JSON.stringify({"errors" : errors, "user" : "ChiltonL"})
    console.log(data_to_save)
    $.ajax({
        type: "POST",
        url: window.location.origin+"/posterrors",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : data_to_save,
        success: function(result){
            console.log(result)
            errors = []
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}
function checkQuiz1(){
    console.log(ingredientsCorrect)
    console.log(ppc_members)
    for (i in ppc_members){
        console.log(ppc_members[i] )
        if (ingredientsCorrect.indexOf(ppc_members[i]) > -1){
            console.log("Right")
        }
        else{
            errors.push({"id" : id, "val":ppc_members[i]})
            console.log("wrong")
        }
    }
    postErrors()
}
function checkQuiz3(){
    console.log(ingredientsCorrect)
    console.log(ppc_members)
    for (i in drink["ingredients"]){
        id = drink["ingredients"][i]['id']
        testid = "#text"+id
        id = "#"+id
        if($(id).val() == drink["ingredients"][i]['amt'] && $(testid).val().toString().toLowerCase() == drink["ingredients"][i]['name'].toLowerCase()){
            console.log("correct")
        }
        else if($(id).val() == drink["ingredients"][i]['amt']){
            errors.push({"id" : id, "val": drink["ingredients"][i]['name'], "amt" : $(testid).val() })
            $(testid).val("INCORRECT");
        }
        else if($(testid).val() == drink["ingredients"][i]['name'].toLowerCase()){
            errors.push({"id" : id, "val": drink["ingredients"][i]['name'], "amt" : $(testid).val() })
            $(id).val("999999999999");
        }
        else{
            errors.push({"id" : id, "val": drink["ingredients"][i]['name'], "amt" : $(testid).val() })
            $(id).val("999999999999");
            $(testid).val("INCORRECT");
            //console.log("y")
        }

    }
    postErrors()
}
function doneButton (){
    nextquiz = parseInt(subStringQuiz())+1
    drink = getRandomInt(length-1)
    console.log(nextquiz)
    console.log(length)
    if(nextquiz > (parseInt(length))) {
        location.href = '/results'
    }
    else {
        location.href = '/quiz/' + nextquiz+"/" +drink
    }
}
function makenames(ingredients, ppc_members){
    $("#ppc").empty()
    $("#non_ppc").empty()
    $.each(ingredients, function(index, value) {
        let employee = $("<div class=person>").draggable({ revert: 'invalid', cursor:"move"})
        $(employee).addClass("nppc")
        $(employee).data("title", value)
        $(employee).data("id", index)
        $(employee).text(value)
        $("#ppc").append(employee)
    })
    $.each(ppc_members, function(index, value) {
        let employee = $("<div class=person>").draggable({ revert: 'invalid', cursor:"move"})
        $(employee).addClass("ppc")
        $(employee).data("title", value)
        $(employee).data("id", index)
        $(employee).text(value)
        $("#non_ppc").append(employee)
    })
}
function subStringQuiz() {
    indx = window.location.href.lastIndexOf('quiz/')
    temp =window.location.href.substring(indx+5,indx+6)
    return (temp);
}
function getRandomInt(max) {
    temp = Math.round(Math.random()*max)
    console.log(temp)
    return (temp);
}
function open_dialogue(correct){
    if(correct){
    $( "#correct_dialog" ).dialog({
        autoOpen: false, 
        buttons: {
            Continue: function() {
                $(this).dialog("close");
                $("#doneButton").click();
            }
        },
        title: "Correct!",
     });
     $('#correct_dialog').dialog('open');
    }
    else{
        $( "#incorrect_dialog" ).dialog({
            autoOpen: false, 
            buttons: {
                Retry: function() {
                    $(this).dialog("close");
                },
                Skip: function() {
                    $(this).dialog("close");
                    $("#doneButton").click();
                }
            },
            title: "Not quite!",
         });
         $('#incorrect_dialog').dialog('open');
    }
}
$(document).ready(function(){
    postVa()
    $("#checkButton").click(function() {
        indx = window.location.href.lastIndexOf('quiz/')
        temp =window.location.href.substring(indx+5,indx+6)
        if (temp == 1){
            checkQuiz1()
        }
        if (temp == 2) {
        checkQuiz2()}
        if (temp == 3) {
            checkQuiz3()}
        if(errors.length===0){
            open_dialogue(1)
        }
        else{
            open_dialogue(0)
        }
    });
    $("#doneButton").click(function() {
        doneButton()
         //might have to change the path
    });
    $("#ppc_drop").droppable({
        drop: function(event, ui){
            console.log(ui.draggable.data("title"))
            ppc_members.push(ui.draggable.data("title"))
            ingredients.splice(ui.draggable.data("id"), 1)
            makenames(ingredients, ppc_members)
        },
        accept: ".nppc"
    })
    $("#nppc_drop").droppable({
        drop: function(event, ui){
                console.log(ui.draggable.data("title"))
                ingredients.push(ui.draggable.data("title"))
                ppc_members.splice(ui.draggable.data("id"), 1)
                makenames(ingredients, ppc_members)
        },
        accept: ".ppc"
    })
})
