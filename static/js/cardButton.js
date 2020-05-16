$(document).ready(()=>{
    $('.like').on('click', function(){
        var liked = this.id
           
            
        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val()
        $.ajax({
            type: "post",
            url: "like",
            data: {'id':liked, 'csrfmiddlewaretoken':csrftoken},
            dataType: "json",
            cache:false,
            success: function (response) {
                var likeCounter = response.count
                if(likeCounter>0){
                  $(`#likeCount${liked}`).text(likeCounter)
                }else{
                    $(`#likeCount${liked}`).text('')
                }
                
                
                
            }
        });
    })

    
})