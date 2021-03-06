

function display_materials(materials, tools, page, title, description){
    $('.header').append("<div class='title text-center title-style'>"+title+"</div>")
    /*if page is 1, put ingredient images and text into a column by only putting */
    if(String(page)==="1"){
        $('.header').append("<div class='description text-center description-space'>"+description+"</div>")
        $("#section").append("<div class='subtitle-style'>Ingredients</div>")
        let cols=0
        $.each(materials, function(index, value){
            cols=cols+1
        })
        let colsize=Math.floor(12/cols)
        $.each(materials, function(index, value){
            let img=value["img"]
            let title=value["name"]
            let to_add="<div class='item-style col-md-"+colsize+"'><img src='"+img+"' alt='"+title+"' class='img img-fluid img-size'><br>"+title+"</div>"
            $("#materials").append(to_add)
        })
        /*add next button*/
        let nextbutton = '<button class="next large-top-margin">Next</button>'
        $('#nextbutton').append(nextbutton)
    }
    /*if page is 2, put materials images and text into a column*/
    else{
        $("#section").append("<div class='subtitle-style'>Tools</div>")
        let cols=0
        $.each(tools, function(index, value){
            cols=cols+1
        })
        let colsize=Math.floor(12/cols)
        $.each(tools, function(index, value){
            let img=value["img"]
            let title=value["name"]
            let to_add="<div class='item-style col-md-"+colsize+"'><img src='"+img+"' alt='"+title+"' class='img img-fluid img-size'><br>"+title+"</div>"
            console.log(to_add)
            $("#materials").append(to_add)
        })
        /*add a next button and a back button*/
        let nextbutton = '<button class="next large-top-margin">Next</button>'
        $('#nextbutton').append(nextbutton)
        let backbutton = '<button class="back large-top-margin">Back</button>'
        $('#backbutton').append(backbutton)
    }
}

function next(page, id){
    let pagenum = page
    if(pagenum<2){
        let nextpage = parseInt(page)
        nextpage = nextpage+1
        window.location.href="/learn/"+id+"/materials/"+nextpage
    }
    else{
        window.location.href="/learn/"+id+"/steps/1"
    }

}
function back(page){
    let prevpage = parseInt(page)
    prevpage = prevpage-1
    window.location.href="/learn/"+id+"/materials/"+prevpage
}

$(document).ready(function(){
    display_materials(materials, tools, page, title, description)

    $(".next").click(function(){
        next(page, id)
    })

    $(".back").click(function(){
        back(page)
    })
})
