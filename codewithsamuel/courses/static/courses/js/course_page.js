var player;
    document.onreadystatechange = function(){
        if(document.readyState == 'interactive'){
            player = document.getElementById("player");
            video_list = document.getElementById("video_list");
        
            mantainRatio()
        }
    }
    
    function mantainRatio(){


        var w = player.clientWidth
        var h = (w*9)/16
        console.log({w, h});
        player.height = h
        video_list.style.maxHeight = h + "px"

    }

    window.onresize = mantainRatio




