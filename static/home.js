
function load_home(data){
    /* list available cocktails with links to learning pages */
    $.each(data, function(index, value){
        let drink_button = "<div class='col'><a class='link-text-style' href='/learn/"+value["id"]+"/materials/1'>"+value["title"]+"<br><img src='"+value["img"]+"' alt='"+value["title"]+"' class='pic img-size'></a><br></div>"
        $("#cocktails").append(drink_button)
    })
}

function get_entry_time(user_data) {
  var today = new Date();
  var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
  var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
  var dateTime = date+' '+time;
  let data_to_save = JSON.stringify({"entry time" : dateTime, "user" : "ChiltonL"})
  $.ajax({
    type: "POST",
    url: window.location.origin+"/posttime",
    dataType : "json",
    contentType: "application/json; charset=utf-8",
    data : data_to_save,
    success: function(result){
        console.log(result)
    },
    error: function(request, status, error){
        console.log("Error");
        console.log(request)
        console.log(status)
        console.log(error)
    }
});
}

function startlearn(){
    window.location.href="/learn/0/materials/1"
}

$(document).ready(function(){
    load_home(data)
    get_entry_time(user_data)
    $("#startbutton").click(function(){
        startlearn()
    })
})
