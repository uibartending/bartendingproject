
function load_home(data){
    /* list available cocktails with links to learning pages */
    $.each(data, function(index, value){
        $("#cocktails").append(value["title"]+'<br>')
    })
}

function startlearn(){
    window.location.href="/learn/0/materials/1"
}

$(document).ready(function(){
    load_home(data)

    $("#startbutton").click(function(){
        startlearn()
    })
})