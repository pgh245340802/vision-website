from yattag import Doc
import os
import sys
import subprocess
import glob

UTILSPATH = "/home/tianxingd/research/ComputerVisionResearch/utils2/"
UNRECTIFIED = ["/computed/decoded/unrectified/proj*/pos*/result[0-9][u,v]-0initial.pfm",
"/computed/decoded/unrectified/proj*/pos*/result[0-9][u,v]-4refined2.pfm",
"/computed/disparity/unrectified/proj*/pos*/disp[0-9][0-9][x,y]-0initial.pfm",
"/computed/disparity/unrectified/proj*/pos*/disp[0-9][0-9][x,y]-1crosscheck.pfm",
"/computed/merged/unrectified/pos*/disp[0-9][0-9][x,y].pfm"]
RECTIFIED = ["/computed/decoded/rectified/proj*/pos*/result[0-9][0-9][u,v]-0rectified.pfm",
"/computed/decoded/rectified/proj*/pos*/result[0-9][0-9][u,v]-4refined2.pfm",
"/computed/disparity/rectified/proj*/pos*/disp[0-9][0-9][x,y]-0initial.pfm",
"/computed/disparity/rectified/proj*/pos*/disp[0-9][0-9][x,y]-3crosscheck2.pfm",
"/computed/merged/rectified/pos*/disp[0-9][0-9][x,y]-0initial.pfm",
"/computed/merged/rectified/pos*/disp[0-9][0-9][x,y]-1crosscheck.pfm",
"/computed/reprojected/proj*/pos*/disp[0-9][0-9]x-0initial.pfm",
"/computed/reprojected/proj*/pos*/disp[0-9][0-9]x-1filtered.pfm",
"/computed/merged2/pos*/disp[0-9][0-9]x-0initial.pfm",
"/computed/merged2/pos*/disp[0-9][0-9]x-4crosscheck2.pfm",]

def duplicate_folders(inputpath, outputpath):
    for dirpath, dirnames, filenames in os.walk(inputpath):
        structure = outputpath + dirpath[len(inputpath):]
        if not os.path.isdir(structure):
            os.mkdir(structure)
        # else:
        #     print("Folder does already exits!")

def convert_pfms(directory):
    dirnames = os.listdir(directory)
    scenes = []
    for dirname in dirnames:
        if dirname[0] != ".":
            scenes.append(dirname)
    scenes.sort()
    # for scenename in scenes:
    #     command = "mkdir ./src/pngs/" + scenename
    #     os.system(command)
    #     inputpath = directory + scenename
    #     outputpath = "./src/pngs/" + scenename
    #     duplicate_folders(inputpath, outputpath)
    #     # -------------------------------------DECODED----------------------------------
    #     for LIST in [UNRECTIFIED[:2], RECTIFIED[:2]]:
    #         for pfm in LIST:
    #             filename= directory + scenename + pfm
    #             sublist = glob.glob(filename)
    #             for file in sublist:
    #                 if os.path.isfile(file):
    #                     txtpath = directory + scenename +"/computed/decoded/unrectified/proj"
    #                     txtpath = txtpath + file[file.find("proj")+4] + "/minmax-%s.txt" % (file[file.rfind("-")-1])
    #                     txt = open(txtpath, "r")
    #                     minmax = txt.read().split()
    #                     savepath = "./src/pngs/" + scenename + file[file.rfind("/computed"):file.rfind(".pfm")]
    #                     pfm2png(file, savepath, minmax[0], minmax[1])
    #                 else:
    #                     print("%s does not exist!!" % (file))

    #     # --------------------------------DISPARITY----------------------------------------
        # for LIST in [UNRECTIFIED[2:], RECTIFIED[2:]]:
        #     for pfm in LIST:
        #         filename= directory + scenename + pfm
        #         sublist = glob.glob(filename)
        #         for file in sublist:
        #             if os.path.isfile(file):
        #                 if file[file.rfind("-")-1] == "x":
        #                     txtpath = directory + scenename +"/computed/merged2/pos"
        #                 else:
        #                     txtpath = directory + scenename +"/computed/merged/rectified/pos"
        #                 txtpath = txtpath + file[file.rfind("disp")+4] + "/minmax-%s.txt" % (file[file.rfind("-")-1])
        #                 txt = open(txtpath, "r")
        #                 minmax = txt.read().split()
        #                 savepath = "./src/pngs/" + scenename + file[file.rfind("/computed"):file.rfind(".pfm")]
        #                 if file[file.rfind("pos")+3] == file[file.rfind("disp")+4]:
        #                     pfm2png(file, savepath, minmax[0], minmax[1])
        #                 else:
        #                     pfm2png(file, savepath, "-"+minmax[0], "-"+minmax[1])
        #             else:
        #                 print("%s does not exist!!" % (file))
            

    #     resize_origs(directory, scenename)
    return scenes

def read_min_max(directory, scenename):
    projpath = directory + scenename +"/computed/decoded/unrectified/proj*"
    projlist = glob.glob(projpath)
    projlist.sort()
    for proj in projlist:
        for i in ["u","v"]:
            mins = []
            maxs = []
            filepath = "%s/pos*/result[0-9]%s-4refined2.pfm" % (proj, i)
            filelist = glob.glob(filepath)
            for file in filelist:
                # imginfo = "../utils2/imginfo"
                imginfo = UTILSPATH + "imginfo"
                min_max = subprocess.check_output([imginfo, "-m", file])
                min_max = min_max.decode().split()
                mins.append(float(min_max[0]))
                maxs.append(float(min_max[1]))
            truemin = str(min(mins))
            truemax = str(max(maxs))
            txtpath = "%s/minmax-%s.txt" % (proj, i)
            txt = open(txtpath, "w")
            txt.write(truemin+"\n")
            txt.write(truemax+"\n")
            txt.close
    

    for i in ["x", "y"]:
        if i == "x":
            path = directory + scenename + "/computed/merged2"
        else:
            path = directory + scenename + "/computed/merged/rectified"
        posnum = len(glob.glob(path+"/pos*"))
        for j in range(posnum-1):
            mins = []
            maxs = []
            pos = str(j)+str(j+1)
            if i == "x":
                filepath = "%s/pos*/disp%s%s-4crosscheck2.pfm" % (path, pos, i)
            else:
                filepath = "%s/pos*/disp%s%s-1crosscheck.pfm" % (path, pos, i)
            filelist = glob.glob(filepath)
            filelist.sort()
            counter = 0
            for file in filelist:
                # imginfo = "../utils2/imginfo"
                imginfo = UTILSPATH + "imginfo"
                min_max = subprocess.check_output([imginfo, "-m", file])
                min_max = min_max.decode().split()
                if counter >0:
                    mins.append(-float(min_max[1]))
                    maxs.append(-float(min_max[0]))
                else:
                    mins.append(float(min_max[0]))
                    maxs.append(float(min_max[1]))
                counter += 1
            truemin = str(min(mins))
            truemax = str(max(maxs))
            txtpath = "%s/pos%s/minmax-%s.txt" % (path, str(j), i)
            txt = open(txtpath, "w")
            txt.write(truemin+"\n")
            txt.write(truemax+"\n")
            txt.close
   
def resize_origs(directory, scenename):
    PATH = directory + scenename + "/orig/calibration/stereo/"
    positions = glob.glob(PATH + "pos*")

    for pos in positions:
        imgs = glob.glob(pos + "/IMG*.JPG")
        for img in imgs:
            smallimg = img.replace(directory, "./src/pngs/")
            if not os.path.isfile(smallimg):
                command = "convert %s -resize 400x400 %s" %(img, smallimg)
                os.system(command)

    PATH = directory + scenename + "/orig/ambient/photos/normal/"
    positions = glob.glob(PATH + "pos*")

    for pos in positions:
        exps = glob.glob(pos + "/exp*")
        for exp in exps:
            imgs = glob.glob(exp + "/IMG*.JPG")
            for img in imgs:
                smallimg = img.replace(directory, "./src/pngs/")
                if not os.path.isfile(smallimg):
                    command = "convert %s -resize 400x400 %s" % (img, smallimg)
                    os.system(command)

def pfm2png(filepath, savepath, minimum, maximum):

    # if os.path.isfile("%s-jet.png" % (savepath)):
    #     print("Jet PNG exists already!")
    # else:
    #     command = "%spfm2png -m %s -d %s -j %s %s-jet.png" % (UTILSPATH, minimum, maximum, filepath, savepath)
    #     os.system(command)

    # if os.path.isfile("%s-spiral.png" % (savepath)):
    #     print("Spiral PNG exists already!")
    # else:
    #     command = "%spfm2png -m %s -d %s -s %s %s-spiral.png" % (UTILSPATH, minimum, maximum, filepath, savepath)
    #     os.system(command)

    # if os.path.isfile("%s-jet-400.jpg" % (savepath)):
    #     print("Resized jet JPG exists already!")
    # else:
    #     command = "convert %s-jet.png -resize 400x400 %s-jet-400.jpg" % (savepath, savepath)
    #     os.system(command)

    # if os.path.isfile("%s-jet-600.jpg" % (savepath)):
    #     print("Resized jet JPG exists already!")
    # else:
    #     command = "convert %s-jet.png -resize 600x600 %s-jet-600.jpg" % (savepath, savepath)
    #     os.system(command)

    # if os.path.isfile("%s-spiral-400.jpg" % (savepath)):
    #     print("Resized jet JPG exists already!")
    # else:
    #     command = "convert %s-spiral.png -resize 400x400 %s-spiral-400.jpg" % (savepath, savepath)
    #     os.system(command)

    # if os.path.isfile("%s-spiral-600.jpg" % (savepath)):
    #     print("Resized jet JPG exists already!")
    # else:
    #     command = "convert %s-spiral.png -resize 600x600 %s-spiral-600.jpg" % (savepath, savepath)
    #     os.system(command)

    command = "%spfm2png -m %s -d %s -j %s %s-jet.png" % (UTILSPATH, minimum, maximum, filepath, savepath)
    os.system(command)

    command = "%spfm2png -m %s -d %s -s %s %s-spiral.png" % (UTILSPATH, minimum, maximum, filepath, savepath)
    os.system(command)

    command = "convert %s-jet.png -resize 400x400 %s-jet-400.jpg" % (savepath, savepath)
    os.system(command)

    command = "convert %s-jet.png -resize 600x600 %s-jet-600.jpg" % (savepath, savepath)
    os.system(command)

    command = "convert %s-spiral.png -resize 400x400 %s-spiral-400.jpg" % (savepath, savepath)
    os.system(command)

    command = "convert %s-spiral.png -resize 600x600 %s-spiral-600.jpg" % (savepath, savepath)
    os.system(command)

def home(directory, scenes):
    home, tag, text = Doc().tagtext()

    home.asis("<!DOCTYPE html>")
    with tag("html"):
        with tag("head"):
            home.asis('<link rel="stylesheet" href="styles.css">')
            with tag("h1"):
                text("Summer 2018 Dataset")
        with tag("body"):
            with tag("p", name="comments"):
                text("THIS DESCRIPTION WILL BE UPDATED")
                home.asis("<br>")
                text("1 image pair with ground truth, shown below at 10% of their original size. Trailing letters indicate dataset types:")
                home.asis("<br>")
                text("P - perfect rectification (imperfect by default);")
                home.asis("<br>")
                text("E - changed exposure between views;")
                home.asis("<br>")
                text("L - changed lighting between views.")
            with tag("p"):
                text("Mouse over the input images to flip between views.")
            with tag("table", style="width: 1080px", border=1, frame="hsides", rules="rows"):
                with tag("tr"):
                    with tag("th"):
                        text("Dataset")
                    with tag("th"):
                        text("Ambient")
                    with tag("th"):
                        text("Final Result Preview")
                    with tag("th"):
                        text("Final Result Preview")
                row = 0
                for scenename in scenes:
                    with tag("tr"):
                        with tag("th", style="width:100px"):
                            text(scenename)
                            decodedpage = decoded(scenename)
                            with tag("a", href=decodedpage, style="display:block"):
                                text("decoded")
                            xdisparity = disparity(scenename, "x")
                            with tag("a", href=xdisparity, style="display:block"):
                                text("X disparity")
                            ydisparity = disparity(scenename, "y")
                            with tag("a", href=ydisparity, style="display:block"):
                                text("Y disparity")
                            calibpage = calibration(directory, scenename)
                            with tag("a", href=calibpage, style="display:block"):
                                text("calibration")
                            
                        with tag("th"):
                            # --------------------------ORIGINAL--------------------------------
                            with tag("div", name="preview-container"):
                                source = "%s%s/orig/ambient/photos/normal/pos0/exp1/IMG1.JPG" % ("./src/pngs/", scenename)
                                with tag("a", href = source.replace("./src/pngs/", directory)):
                                    home.stag("img", src=source, klass="row"+str(row), id= "orig"+str(row), style = "display: block")
                                pospath = "%s%s/orig/ambient/photos/normal/pos*" % ("./src/pngs/", scenename)
                                positions = glob.glob(pospath)
                                positions.sort()
                                position = 0
                                with tag("div", name="caption-container-home"+str(row), klass = "caption-container"):
                                    text("pos"+str(position))
                                for pos in positions:
                                    no = 0
                                    with tag("div", name="thumbnail-container"):
                                        img = "%s/exp1/IMG1.JPG" % (pos)
                                        with tag("a", href = img.replace("./src/pngs/", directory)):
                                            home.stag("img", src=img, klass="row"+str(row), name="thumbnail", 
                                            id="thumb"+str(row)+str(position)+str(no), 
                                            onmouseover="posUpdateHome(%s, %s, %s, %s)" % ("orig"+str(row), str(row),str(position), str(no)))
                                    position += 1

                        with tag("th"):
                            source = "./src/pngs/%s/computed/merged2/pos0/disp01x-4crosscheck2-jet-400.jpg" % (scenename)
                            imageBoxDual(home, tag, text, "x"+str(row), source, 1, row)                            # imageBoxDual(home, tag, text, "u"+str(row), source, 1, row)

                        with tag("th"):
                            source = "./src/pngs/%s/computed/merged2/pos1/disp01x-4crosscheck2-jet-400.jpg" % (scenename)
                            imageBoxDual(home, tag, text, "x"+str(row), source, 2, row, reverse=True)   

                    row += 1

            home.asis('<script type="text/javascript" src="master.js"></script>')

    HTML = home.getvalue()
    file = open("home.html", "w")
    file.write(HTML)
    file.close()

def imageBox(doc, tag, text, name, source, no, row, rec = "rec"):
    with tag("div", name="preview-container"):
        with tag("p", name="imgtext"+str(row), klass="imgtext"):
            text(source[source.rfind("/")+1:])
        with tag("a", href = source.replace("-400.jpg", ".png"), name="imglink"+str(row), klass="imglink"):
            class1 = "row"+str(row)+" "
            doc.stag("img", src=source, klass=class1 + rec, id= name, name=str(row), style="display:block")
        pospath = source[:source.rfind("pos0/") + 3] + "*"
        positions = glob.glob(pospath)
        positions.sort()
        position = 0
        with tag("div", name="caption-container"+str(row), klass = "caption-container"):
            text("pos"+str(position))
        for pos in positions:
            with tag("div", name="thumbnail-container"):
                tag1 = source[source.rfind("/")+1:source.rfind("0", 0, source.find("-"))]
                firstindex = source.find("-")
                secondindex = source.find("-", firstindex+1)
                tag2 = source[firstindex+1:secondindex]
                img = "%s/%s%s%s-%s-jet-400.jpg" % (pos, tag1, str(position), name[0],tag2)
                with tag("a", href = img.replace("-400.jpg", ".png"), klass="imglink"):
                    doc.stag("img", src=img, klass=class1 + rec, name=rec, id="thumb"+str(row)+str(position)+str(no), 
                    onmouseover="posUpdate('%s', %s)" % (str(row), str(position)))
            position += 1

def imageBoxDual(doc, tag, text, name, source, no, row, rec="rec", reverse=False):
    with tag("div", name="preview-container"):
        with tag("p", name="imgtext"+str(row), klass="imgtext"):
            text(source[source.rfind("/")+1:])
        with tag("a", href = source.replace("-400.jpg", ".png"), name="imglink"+str(row), klass="imglink"):
            class1 = "row"+str(row)+" "
            doc.stag("img", src=source, klass=class1 + rec, id=name, name=str(row), style="display:block")
        pospath = source[:source.rfind("pos") + 3] + "*"
        positions = glob.glob(pospath)
        positions.sort()
        position = 0
        if reverse:
            with tag("div", name="caption-container"+str(row), klass = "caption-container"):
                text("pos"+str(position+1)+str(position))
        else:
            with tag("div", name="caption-container"+str(row), klass = "caption-container"):
                text("pos"+str(position)+str(position+1))
        for pos in positions:
            tag1 = source[source.rfind("/")+1:source.rfind("0", 0, source.find("-"))]
            if source.count("-") >= 2:
                firstindex = source.find("-")
                secondindex = source.find("-", firstindex+1)
                tag2 = source[firstindex:secondindex]
            else:
                tag2 = ""
            if reverse:
                if pos != positions[0]:
                    img = "%s/%s%s%s%s-jet-400.jpg" % (pos, tag1, str(position-1)+str(position), name[0],tag2)
                    if os.path.isfile(img):
                        with tag("div", name="thumbnail-container"):
                            with tag("a", href = img.replace("-400.jpg", ".png"), klass="imglink"):
                                doc.stag("img", src=img, klass=class1 + rec, 
                                id="thumb"+str(row)+str(position)+str(position-1)+str(no), 
                                onmouseover="posUpdateDisp('%s', '%s')" % (str(row), str(position-1)+str(position)))

            else:
                img = "%s/%s%s%s%s-jet-400.jpg" % (pos, tag1, str(position)+str(position+1), name[0],tag2)
                if os.path.isfile(img):
                    with tag("div", name="thumbnail-container"):    
                        with tag("a", href = img.replace("-400.jpg", ".png"), klass="imglink"):
                            doc.stag("img", src=img, klass=class1 + rec,
                            id="thumb"+str(row)+str(position)+str(position+1)+str(no), 
                            onmouseover="posUpdateDisp('%s', '%s')" % (str(row), str(position)+str(position+1)))
            position += 1

def disparity(scenename, xy):
    doc, tag, text = Doc().tagtext()
    doc.asis("<!DOCTYPE html>")

    with tag("html"):
        with tag("head"):
            doc.asis('<link rel="stylesheet" href="styles.css">')
            with tag("h1"):
                text(scenename)
        with tag("body"):
            with tag("h2"):
                text("Scene photos")
            with tag("h3"):
                text("Description:")
            with tag("p"):
                text("""This webpage displays all relevant images in the image processing pipeline. 
                On the left, mouse over different previews to see different projector positions. 
                Below each main image, mouse over the previews to see different camera positions.
                The tags also show you which image you are viewing. If the position is identified with three digits, e.g. pos223,
                it means that you are viewing the processed image between different camera positions. The last two digits suggest
                the positions referenced, and the first one indicate the position folder it came from. In this case, pos223 means that
                it is processed from images from position 2 and 3, and it comes from the folder pos2, which means that pos2 is used as the left position.""")
            with tag("p"):
                text("""The following buttons and selector can be used to select which images to appear on the website""")
            with tag("button", onclick = "hideAndShow('rec','unrec')"):
                text("Show Unrectified Only")
            with tag("button", onclick = "hideAndShow('unrec','rec')"):
                text("Show Rectified Only")
            with tag("button", onclick = "unhide('unrec','rec')"):
                text("Show all")
            with tag("select", onchange="changeSize(value)"):
                with tag("option", value = 400):
                    text("Display images in size 400")
                with tag("option", value = 600):
                    text("Display images in size 600")
            with tag("select", onchange="changeCol(value)"):
                with tag("option", value = "jet"):
                    text("Display images in jet")
                with tag("option", value = "spiral"):
                    text("Display images in spiral")
            with tag("div", name = "line-container"):
                for LIST in [UNRECTIFIED[2:], RECTIFIED[2:]]:
                    for imgtag in LIST:
                        filename= "./src/pngs/" + scenename + imgtag.replace(".pfm", "*")
                        sublist = glob.glob(filename)
                        for file in sublist:
                            if os.path.isfile(file):
                                doc.stag("img", href = file, klass = "line-img")

            with tag("table", cellpadding = "-10", cellspacing = "-10", border=1, frame="hsides", rules="rows"):
                with tag("tr", klass = "space"):
                    with tag("th", klass = "proj"):
                        text("proj")
                    with tag("th", klass = "imgbox-container"):
                        text("View 01")
                    with tag("th", klass = "imgbox-container"):
                        text("View 10")
                row = 0

                for LIST in [UNRECTIFIED[2:], RECTIFIED[2:]]:
                    if LIST == UNRECTIFIED[2:]:
                        rec = "unrec"
                    else:
                        rec = "rec"
                    for file in LIST:
                        filename= "./src/pngs/" + scenename + file.replace(".pfm", "-jet-400.jpg")
                        sublist = glob.glob(filename)
                        sublist.sort()
                        if sublist != []:
                            with tag("tr", klass=rec):
                                source = sublist[0].replace("01x", "01"+xy)
                                if os.path.isfile(source):
                                    with tag("th", klass = "proj"):
                                        if "/proj*/" in file:
                                            projlist = glob.glob(filename[:filename.rfind("/pos")])
                                            projlist.sort()
                                            with tag("div", name="projnum-container"+str(row), klass = "projnum-container"):
                                                text("proj0")
                                            for i in projlist:
                                                source = sublist[0]
                                                imgtag = source[source.rfind("pos0/")+5:]
                                                img = i + "/pos0/" + imgtag
                                                proj = i[i.rfind("proj"):]
                                                with tag("div", name="thumbnail-container-vertical"):
                                                    with tag("a", href = img.replace("-400.jpg", "-jet.png")):
                                                        doc.stag("img", src=img, name=rec, id="proj"+str(proj[-1]),
                                                        onmouseover = "projChange(%s, %s)" % (proj[-1], str(row)))
                                
                                if os.path.isfile(source):        
                                    with tag("th", klass = "imgbox-container"):
                                        source = sublist[0].replace("01x", "01"+xy)
                                        imageBoxDual(doc, tag, text, xy+str(row), source, 1, row, rec)

                                source = source.replace("pos0", "pos1")
                                if os.path.isfile(source):
                                    with tag("th", klass = "imgbox-container"):
                                        imageBoxDual(doc, tag, text, xy+str(row), source, 2, row, rec, reverse=True)
                            row += 1

            doc.asis('<script type="text/javascript" src="master.js"></script>')

    HTML = doc.getvalue()
    filename= scenename + "-%sdisparity.html" % (xy)
    file = open(filename, "w")
    file.write(HTML)
    file.close()
    return filename

def decoded(scenename):
    doc, tag, text = Doc().tagtext()
    doc.asis("<!DOCTYPE html>")

    with tag("html"):
        with tag("head"):
            doc.asis('<link rel="stylesheet" href="styles.css">')
            with tag("h1"):
                text(scenename)
        with tag("body"):
            with tag("h2"):
                text("Scene photos")
            with tag("h3"):
                text("Description:")
            with tag("p"):
                text("""This webpage displays all relevant images in the image processing pipeline. 
                On the left, mouse over different previews to see different projector positions. 
                Below each main image, mouse over the previews to see different camera positions.
                The tags also show you which image you are viewing. If the position is identified with three digits, e.g. pos223,
                it means that you are viewing the processed image between different camera positions. The last two digits suggest
                the positions referenced, and the first one indicate the position folder it came from. In this case, pos223 means that
                it is processed from images from position 2 and 3, and it comes from the folder pos2, which means that pos2 is used as the left position.""")
            with tag("p"):
                text("""The following buttons and selector can be used to select which images to appear on the website""")
            with tag("button", onclick = "hideAndShow('rec','unrec')"):
                text("Show Unrectified Only")
            with tag("button", onclick = "hideAndShow('unrec','rec')"):
                text("Show Rectified Only")
            with tag("button", onclick = "unhide('unrec','rec')"):
                text("Show all")
            with tag("select", onchange="changeSize(value)"):
                with tag("option", value = 400):
                    text("Display images in size 400")
                with tag("option", value = 600):
                    text("Display images in size 600")
            with tag("select", onchange="changeCol(value)"):
                with tag("option", value = "jet"):
                    text("Display images in jet")
                with tag("option", value = "spiral"):
                    text("Display images in spiral")
            with tag("div", name = "line-container"):
                for LIST in [UNRECTIFIED[:2], RECTIFIED[:2]]:
                    for imgtag in LIST:
                        filename= "./src/pngs/" + scenename + imgtag.replace(".pfm", "*")
                        sublist = glob.glob(filename)
                        for file in sublist:
                            if os.path.isfile(file):
                                doc.stag("img", href = file, klass = "line-img")

            with tag("table", cellpadding = "-10", cellspacing = "-10", border=1, frame="hsides", rules="rows"):
                with tag("tr", klass = "space"):
                    with tag("th", klass = "proj"):
                        text("proj")
                    with tag("th", klass = "imgbox-container"):
                        text("u/x")
                    with tag("th", klass = "imgbox-container"):
                        text("v/y")
                row = 0

                for LIST in [UNRECTIFIED[:2], RECTIFIED[:2]]:
                    if LIST == UNRECTIFIED[:2]:
                        rec = "unrec"
                    else:
                        rec = "rec"
                    for file in LIST:
                        filename= "./src/pngs/" + scenename + file.replace(".pfm", "-jet-400.jpg")
                        sublist = glob.glob(filename)
                        sublist.sort()
                        if sublist != []:
                            with tag("tr", klass=rec):
                                
                                with tag("th", klass = "proj"):
                                    if "/proj*/" in file:
                                        projlist = glob.glob(filename[:filename.rfind("/pos")])
                                        projlist.sort()
                                        with tag("div", name="projnum-container"+str(row), klass = "projnum-container"):
                                            text("proj0")
                                        for i in projlist:
                                            source = sublist[0]
                                            imgtag = source[source.rfind("pos0/")+5:]
                                            img = i + "/pos0/" + imgtag
                                            proj = i[i.rfind("proj"):]
                                            with tag("div", name="thumbnail-container-vertical"):
                                                with tag("a", href = img.replace("-400.jpg", ".png")):
                                                    doc.stag("img", src=img, name=rec, id="proj"+str(proj[-1]),
                                                    onmouseover = "projChange(%s, %s)" % (proj[-1], str(row)))
                                        
                                    

                                with tag("th", klass = "imgbox-container"):
                                    source = sublist[0]
                                    if "[u,v]" in file:
                                        if "[0-9][0-9]" not in file:
                                            imageBox(doc, tag, text, "u"+str(row), source, 1, row, rec)
                                        else:
                                            imageBoxDual(doc, tag, text, "u"+str(row), source, 1, row, rec)
                                    else:
                                        if "[0-9][0-9]" not in file:
                                            imageBox(doc, tag, text, "x"+str(row), source, 1, row, rec)
                                        else:
                                            imageBoxDual(doc, tag, text, "x"+str(row), source, 1, row, rec)

                                with tag("th", klass = "imgbox-container"):
                                    source = sublist[1]
                                    if "[u,v]" in file:
                                        if "[0-9][0-9]" not in file:
                                            imageBox(doc, tag, text, "v"+str(row), source, 2, row, rec)
                                        else:
                                            imageBoxDual(doc, tag, text, "v"+str(row), source, 2, row, rec, reverse=True)
                                    elif "[x,y]" in file:
                                        if "[0-9][0-9]" not in file:
                                            imageBox(doc, tag, text, "y"+str(row), source, 2, row, rec)
                                        else:
                                            imageBoxDual(doc, tag, text, "y"+str(row), source, 2, row, rec, reverse=True)
                            row += 1

            doc.asis('<script type="text/javascript" src="master.js"></script>')

    HTML = doc.getvalue()
    filename= scenename + "-decoded.html"
    file = open(filename, "w")
    file.write(HTML)
    file.close()
    return filename

def calibration(directory, scenename):
    doc, tag, text = Doc().tagtext()
    doc.asis("<!DOCTYPE html>")

    PATH = "./src/pngs/" + scenename + "/orig/calibration/stereo/"
    positions = glob.glob(PATH + "pos*")
    positions.sort()

    with tag("html"):
        with tag("head"):
            doc.asis('<link rel="stylesheet" href="styles.css">')
            with tag("h1"):
                text(scenename)
        with tag("body"):
            with tag("h2"):
                text("Stereo calibration photos")
            with tag("div", name="table-container"):
                with tag("table"):
                    with tag("tr"):
                        for pos in positions:
                            with tag("th"):
                                with tag("div", name="view-container"):
                                    source = pos + "/IMG0.JPG"
                                    doc.stag("img", src=source, name="views", id=pos[-4:-1]+pos[-1])

                position = 0
                num_views = len(positions)
                with tag("table"):
                    for pos in positions:
                        imgs = glob.glob(pos + "/IMG*.JPG")
                        imgs.sort()
                        no = 0
                        with tag("tr"):
                            for img in imgs:
                                with tag("th"):
                                    with tag("div", name="thumbnail-container"):
                                        doc.stag("img", src=img, name="thumbnail", id="thumb"+str(position)+str(no), onmouseover="changeView("+str(num_views)+","+str(no)+")")
                                no = no + 1
                        position = position + 1
            doc.asis('<script type="text/javascript" src="master.js"></script>')

    HTML = doc.getvalue()
    filename= scenename + "-calib.html"
    file = open(filename, "w")
    file.write(HTML)
    file.close()
    return filename

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 generate-web.py [path of scene folder]")
    directory = sys.argv[1]
    if directory[-1] != "/":
        directory = directory + "/"
    read_min_max(directory,"animals2")
    scenes = convert_pfms(directory)
    home(directory, scenes)