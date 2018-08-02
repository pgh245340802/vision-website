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

function posUpdateDisp(name, pos) {
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
}

function projChange(value, row) {
    var captions = document.getElementsByName("projnum-container"+row)
    for (var i=0; i<captions.length; i++) {
        captions[i].innerHTML = "proj" + value
    }
    var images = document.getElementsByClassName("row"+row)
    for (var i=0; i<images.length; i++) {
        var source = images[i].src
        source = source.replace(/proj[0-9]/, "proj"+value)
        images[i].src = source
    }
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