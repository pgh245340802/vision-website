function changeView(pos, img) {
    var i;
    for (i = 0; i < pos; i ++){
        var image = "thumb" + i + img;
        var position = "pos" + i;
        document.getElementById(position).src = document.getElementById(image).src
    }
}

function posUpdateHome(name, row, pos, no) {
    var captions = document.getElementsByName("caption-container-home"+row)
    for (var i=0; i<captions.length; i++) {
        captions[i].innerHTML = "pos" + pos
    }
    var image = "thumb" + row + pos + no;
    name.src = document.getElementById(image).src
}

function posUpdate(name, pos) {
    var captions = document.getElementsByName("caption-container"+name)
    var images = document.getElementsByName(name)
    var links = document.getElementsByName("imglink"+name)
    var texts = document.getElementsByName("imgtext"+name)
    for (var i=0; i<links.length; i++) {
        var no = i + 1
        var image = "thumb" + name + pos + no;
        captions[i].innerHTML = "pos" + pos
        images[i].src = document.getElementById(image).src;
        newlink = document.getElementById(image).src
        newlink = newlink.substring(0,newlink.lastIndexOf("-")) + ".png"
        links[i].href = newlink
        newname = document.getElementById(image).src
        newname = newname.substring(newname.lastIndexOf("/")+1,)
        texts[i].innerHTML = newname
    }

}

function posUpdateDisp(name, pos, disparity = false, rec = 'rec') {
    var captions = document.getElementsByName("caption-container"+name)
    var images = document.getElementsByName(name)
    var links = document.getElementsByName("imglink"+name)
    var texts = document.getElementsByName("imgtext"+name)
    for (var i = 0; i < captions.length; i++){
        if (i == 1){
            pos = pos[1] + pos[0]
        }
        var no = i + 1
        captions[i].innerHTML = "pos" + pos
        image = "thumb" + name + pos + no;
        images[i].src = document.getElementById(image).src;
        newlink = document.getElementById(image).src
        newlink = newlink.substring(0,newlink.lastIndexOf("-")) + ".png"
        links[i].href = newlink
        newname = document.getElementById(image).src
        newname = newname.substring(newname.lastIndexOf("/")+1,)
        texts[i].innerHTML = newname
    }

    if(disparity){
      var minmax = document.getElementsByName("minmaxx"+name).length > 0? document.getElementsByName("minmaxx"+name):document.getElementsByName("minmaxy"+name)
      var newminmax = document.getElementsByName("maxmin-"+rec+"-pos"+pos.slice(1, 2))[0].innerText

      for (var i = 0; i < minmax.length; i++){
        if(i == 1){
          negated = []
          negated.push(-parseFloat(newminmax.split(",")[0].replace(/^\s+|\s+$|^\[+|\]+$/gm,'')))
          negated.push(-parseFloat(newminmax.split(",")[1].replace(/^\s+|\s+$|^\[+|\]+$/gm,'')))
          newminmax = "[" + negated.join() + "]"
        }
        minmax[i].innerHTML = newminmax
      }
    }
}

function posUpdateAmb(name, pos) {
    var captions = document.getElementsByName("caption-container"+name)
    var images = document.getElementsByName(name)
    var texts = document.getElementsByName("imgtext"+name)
    for (var i = 0; i < captions.length; i++){
        if (i == 1){
            pos = pos[1] + pos[0]
        }
        var no = i + 1
        captions[i].innerHTML = "pos" + pos
        image = "thumb" + name + pos + no
        images[i].src = document.getElementById(image).src;
        newname = document.getElementById(image).src
        newname = newname.substring(newname.lastIndexOf("/")+1,)
        texts[i].innerHTML = newname
    }
}



function projChange(value, row, decoded = false) {
    var captions = document.getElementsByName("projnum-container"+row)
    for (var i=0; i<captions.length; i++) {
        captions[i].innerHTML = "proj" + value
    }
    var images = document.getElementsByClassName("row"+row)
    var links = document.getElementsByName("imglink"+row)

    for (var i=0; i<images.length; i++) {
        var source = images[i].src
        source = source.replace(/proj[0-9]/, "proj"+value)
        images[i].src = source
    }
    for(var i=0; i<links.length; i++){
        var newlink = source.substring(0,source.lastIndexOf("-")) + ".png"
	links[i].href = newlink
    }

    if(decoded){
      var minmax_u = document.getElementsByName("minmaxu"+row)
      minmax_u[0].innerHTML = document.getElementsByName("maxmin-u"+value)[0].innerText
      var minmax_v = document.getElementsByName("minmaxv"+row)
      minmax_v[0].innerHTML = document.getElementsByName("maxmin-v"+value)[0].innerText
    }
}

function expChange(value, row, rec=false) {
    var captions = document.getElementsByName("exp-caption-container"+row)
    for (var i=0; i<captions.length; i++) {
        captions[i].innerHTML = "exp" + value
    }
    var images = document.getElementsByClassName("row"+row)
    for (var i=0; i<images.length; i++) {
        var source = images[i].src
        source = source.replace(/exp[0-9]/, "exp"+value)
        images[i].src = source
    }
    if(rec){
	var name = document.getElementsByName("imgtext"+row)
        newname = source.substring(source.lastIndexOf("/")+1,)
        name[0].innerHTML = newname
	name[1].innerHTML = newname
	var images = document.getElementsByClassName("row"+row)
	var links = document.getElementsByName("imglink"+row)

	for (var i=0; i<images.length; i++) {
            var source = images[i].src
            source = source.replace(/proj[0-9]/, "proj"+value)
            images[i].src = source
	}
	for(var i=0; i<links.length; i++){
            var newlink = source.substring(0,source.lastIndexOf("-")) + ".png"
	    links[i].href = newlink
	}
    }
}

function swapBall(x) {

    x.src = x.src.replace('ambient',"ambientBall")
    
}

function restoreBall(x) {

    x.src = x.src.replace('ambientBall',"ambient")
    
}



function swap(x,reverse){

    var pos = x.src.charAt(x.src.indexOf("pos")+3)
    pos = reverse ? parseInt(pos)-1:parseInt(pos)+1
    x.src = x.src.replace(/pos[0-9]/,"pos"+pos)

}

function restore(x,reverse){

    var pos = x.src.charAt(x.src.indexOf("pos")+3)
    pos = reverse ? parseInt(pos)+1:parseInt(pos)-1
    x.src = x.src.replace(/pos[0-9]/,"pos"+pos)

}

function hideAndShow(hide,show) {
    var images = document.getElementsByClassName(hide)
    for (var i=0; i<images.length; i++) {
        images[i].style.display = "none"
    }
    var images = document.getElementsByClassName(show)
    for (var i=0; i<images.length; i++) {
        images[i].style.display = ""
        if (images[i].width > 100) {
            images[i].style.display = "block"
        }
    }
}

function unhide() {
    for (var i=0; i<arguments.length; i++) {
        var images = document.getElementsByClassName(arguments[i])
        for (var j=0; j<images.length; j++) {
            images[j].style.display = ""
            if (images[i].width > 100) {
                images[i].style.display = "block"
            }
        }
    }
}

function changeCol(value) {
    if (value == "spiral"){
        var images = document.getElementsByTagName("img")
        for (var i=0; i<images.length; i++) {
            images[i].src = images[i].src.replace("-jet", "-spiral")
        }
        var texts = document.getElementsByClassName("imgtext")
        for (var i=0; i<texts.length; i++) {
            texts[i].innerHTML = texts[i].innerHTML.replace("-jet", "-spiral")
        }
        var links = document.getElementsByClassName("imglink")
        for (var i=0; i<texts.length; i++) {
            links[i].href = links[i].href.replace("-jet", "-spiral")
        }
    } else {
        var images = document.getElementsByTagName("img")
        for (var i=0; i<images.length; i++) {
            images[i].src = images[i].src.replace("-spiral", "-jet")
        }
        var texts = document.getElementsByClassName("imgtext")
        for (var i=0; i<texts.length; i++) {
            texts[i].innerHTML = texts[i].innerHTML.replace("-spiral", "-jet")
        }
        var links = document.getElementsByClassName("imglink")
        for (var i=0; i<texts.length; i++) {
            links[i].href = links[i].href.replace("-spiral", "-jet")
        }
    }
}

function changeSize(value) {
    if (value == 600){
        var images = document.getElementsByTagName("img")
        for (var i=0; i<images.length; i++) {
            images[i].src = images[i].src.replace("-400", "-600")
        }
        var texts = document.getElementsByClassName("imgtext")
        for (var i=0; i<texts.length; i++) {
            texts[i].innerHTML = texts[i].innerHTML.replace("-400", "-600")
        }
    } else {
        var images = document.getElementsByTagName("img")
        for (var i=0; i<images.length; i++) {
            images[i].src = images[i].src.replace("-600", "-400")
        }
        var texts = document.getElementsByClassName("imgtext")
        for (var i=0; i<texts.length; i++) {
            texts[i].innerHTML = texts[i].innerHTML.replace("-600", "-400")
        }
    }
}
