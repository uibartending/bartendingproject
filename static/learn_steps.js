
function display_step(step, page, materials, tools){
    /* print the step for the corresponding page */
    $("#instruction").append("STEP "+page+":<br>")
    $("#instruction").append(step["text"])
    /* put in the images for the tools and ingredients req */
    $.each(step["ingredients"], function(index, value){
        $.each(materials, function(i,v){
            console.log("material matches needed ing")
            if(v["name"].toLowerCase()===value.toLowerCase()){
                let img=v["img"]
                let to_append="<div class='col'><img src='"+img+"' alt='"+value+"' class='img img-fluid'></img></div>"
                $("#ing_images").append(to_append)
            }
        })
    })
    $.each(step["tools"], function(index, value){
        $.each(tools, function(i,v){
            console.log("tool matches needed ing")
            if(v["name"].toLowerCase()===value.toLowerCase()){
                let img=v["img"]
                let to_append="<div class='col'><img src='"+img+"' alt='"+value+"' class='img img-fluid'></img></div>"
                $("#tool_images").append(to_append)
            }
        })
    })
    /* put in next column visuals */
    $.each(step["img"], function(index, value){
        let alt="filler"
        let to_append="<div class='col'><img src='"+value+"' alt='"+alt+"' class='img img-fluid'></img></div>"
        $("#visuals").append(to_append)
    })
}

$(document).ready(function(){
    display_step(step, page, materials, tools)
})