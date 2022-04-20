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
var ingredientsCorrect = [
]
var id = 1
function getclient(){
    let data_to_save = JSON.stringify({"id":id})
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
            console.log(ingredients)
            console.log(result)
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


function makenames(ingredients, ppc_members){
    $("#ppc").empty()
    $("#non_ppc").empty()
    $.each(ingredients, function(index, value) {
        let employee = $("<div class=person>").draggable({ revert: 'invalid', cursor:"move"})
        $(employee).addClass("nppc")
        $(employee).data("name", value)
        $(employee).data("num", index)
        $(employee).text((index+1)+". "+value)
        $("#ppc").append(employee)
    })
    $.each(ppc_members, function(index, value) {
        let employee = $("<div class=person>").draggable({ revert: 'invalid', cursor:"move"})
        $(employee).addClass("ppc")
        $(employee).data("name", value)
        $(employee).data("num", index)
        $(employee).text((index+1)+". "+value)
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
$(document).ready(function(){
    getclient()

    $("#doneButton").click(function() {
        nextquiz = parseInt(subStringQuiz())+1
        drink = getRandomInt(length-1)
        if(nextquiz > (length)) {
            location.href = '/'
        }
        else {
            location.href = '/quiz/' + nextquiz+"/" +drink
        }
         //might have to change the path
    });
    $("#ppc_drop").droppable({
        drop: function(event, ui){
            console.log(ui.draggable.data("name"))
            ppc_members.push(ui.draggable.data("name"))
            ingredients.splice(ui.draggable.data("num"), 1)
            makenames(ingredients, ppc_members)
        },
        accept: ".nppc"
    })
    $("#nppc_drop").droppable({
        drop: function(event, ui){
                console.log(ui.draggable.data("name"))
                ingredients.push(ui.draggable.data("name"))
                ppc_members.splice(ui.draggable.data("num"), 1)
                makenames(ingredients, ppc_members)
        },
        accept: ".ppc"
    })
})
