

function display_materials(materials, tools, page){
    /*if page is 1, put ingredient images and text into a column by only putting */
    if(String(page)==="1"){
        $("#section").append("Ingredients")
        let cols=0
        $.each(materials, function(index, value){
            cols=cols+1
        })
        let colsize=Math.floor(12/cols)
        $.each(materials, function(index, value){
            let img=value["img"]
            let title=value["name"]
            let to_add="<div class='col-md-"+colsize+"'><img src='"+img+"' alt='"+title+"' class='img img-fluid'><br>"+title+"</div>"
            $("#materials").append(to_add)
        })
        /*add next button*/
    } 
    /*if page is 2, put materials images and text into a column*/
    else{
        $("#section").append("Tools")
        let cols=0
        $.each(tools, function(index, value){
            cols=cols+1
        })
        let colsize=Math.floor(12/cols)
        $.each(tools, function(index, value){
            let img=value["img"]
            let title=value["name"]
            let to_add="<div class='col-md-"+colsize+"'><img src='"+img+"' alt='"+title+"' class='img img-fluid'><br>"+title+"</div>"
            console.log(to_add)
            $("#materials").append(to_add)
        })
        /*add a next button and a back button*/
    }
}

$(document).ready(function(){
    display_materials(materials, tools, page)
})