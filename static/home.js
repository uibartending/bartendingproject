
function load_home(data){
    /* list available cocktails with links to learning pages */
    $.each(data, function(index, value){
        $("#cocktails").append(value["title"]+'<br>')
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
