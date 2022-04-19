employees = [
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

let ppc_members=[]

function makenames(employees, ppc_members){
    $("#ppc").empty()
    $("#non_ppc").empty()
    $.each(employees, function(index, value) {
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

$(document).ready(function(){
    makenames(employees, ppc_members)
    $("#ppc_drop").droppable({
        drop: function(event, ui){
            console.log(ui.draggable.data("name"))
            ppc_members.push(ui.draggable.data("name"))
            employees.splice(ui.draggable.data("num"), 1)
            makenames(employees, ppc_members)
        },
        accept: ".nppc"
    })
    $("#nppc_drop").droppable({
        drop: function(event, ui){
                console.log(ui.draggable.data("name"))
                employees.push(ui.draggable.data("name"))
                ppc_members.splice(ui.draggable.data("num"), 1)
                makenames(employees, ppc_members)
        },
        accept: ".ppc"
    })
})
