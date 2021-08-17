
import random
from gl import Renderer, V2
from obj import Object

windoWidth = 1920*1
windowHeight = 1080*1
scale= 1
viewportWidth= windoWidth*scale
viewportHeight= windowHeight *scale
viewportX=0
viewportY=0


poligon1 = [V2(165, 380) ,V2(185, 360),V2 (180, 330),V2 (207, 345),V2 (233, 330),V2 (230, 360),V2 (250, 380),V2 (220, 385) ,V2(205, 410),V2 (193, 383)]
poligon2 = [V2(321, 335),V2 (288, 286),V2 (339, 251),V2 (374, 302)]
poligon3 =[V2(377, 249),V2 (411, 197),V2 (436, 249)]
poligon4=[V2(413, 177) ,V2(448, 159) ,V2(502, 88) ,V2(553, 53) ,V2(535, 36) ,V2(676, 37) ,V2(660, 52)
,V2(750, 145),V2 (761, 179),V2 (672, 192) ,V2(659, 214),V2 (615, 214),V2 (632, 230),V2 (580, 230)
,V2(597, 215) ,V2(552, 214) ,V2(517, 144) ,V2(466, 180)]


poligon5= [V2(682, 175),V2 (708, 120) ,V2(735, 148) ,V2(739, 170)]


shrek= [V2(0,520),V2(100,490),V2(145,470),V2(175,410),V2(200,320),V2(225,220)]
#draw the star
def drawPoligon1():
    for vert in poligon1:
        myRenderer.glVertex(vert.x,vert.y)
    myRenderer.glFillTriangle(poligon1[1],poligon1[2],poligon1[3])
    myRenderer.glFillTriangle(poligon1[3],poligon1[4],poligon1[5])
    myRenderer.glFillTriangle(poligon1[5],poligon1[6],poligon1[7])
    myRenderer.glFillTriangle(poligon1[7],poligon1[8],poligon1[9])
    myRenderer.glFillTriangle(poligon1[9],poligon1[0],poligon1[1])

    myRenderer.glFillTriangle(poligon1[1],poligon1[3],poligon1[9])
    myRenderer.glFillTriangle(poligon1[3],poligon1[7],poligon1[9])
    myRenderer.glFillTriangle(poligon1[3],poligon1[7],poligon1[5])

#square
def drawPoligon2():
    for vert in poligon2:
        myRenderer.glVertex(vert.x,vert.y)

    myRenderer.glFillTriangle(poligon2[0],poligon2[1],poligon2[2])
    myRenderer.glFillTriangle(poligon2[0],poligon2[2],poligon2[3])

#triangle
def drawPoligon3():
    for vert in poligon3:
        myRenderer.glVertex(vert.x,vert.y)
    myRenderer.glFillTriangle(poligon3[0],poligon3[1],poligon3[2])

#teapot
def drawPoligon4():
    for vert in poligon4:
        myRenderer.glVertex(vert.x,vert.y)

    for i in range(len(poligon4)-1):
        myRenderer.glLine(poligon4[i].x,poligon4[i].y,poligon4[i+1].x,poligon4[i+1].y,)

    myRenderer.glFillTriangle(poligon4[0],poligon4[1],poligon4[17])
    myRenderer.glFillTriangle(poligon4[1],poligon4[16],poligon4[17])
    myRenderer.glFillTriangle(poligon4[1],poligon4[2],poligon4[16])
    myRenderer.glFillTriangle(poligon4[2],poligon4[3],poligon4[16])
    myRenderer.glFillTriangle(poligon4[3],poligon4[15],poligon4[16])
    myRenderer.glFillTriangle(poligon4[3],poligon4[4],poligon4[5])
    myRenderer.glFillTriangle(poligon4[3],poligon4[5],poligon4[6])
    myRenderer.glFillTriangle(poligon4[3],poligon4[6],poligon4[15])


    myRenderer.glFillTriangle(poligon4[12],poligon4[13],poligon4[14])
    myRenderer.glFillTriangle(poligon4[11],poligon4[12],poligon4[14])

    myRenderer.glFillTriangle(poligon4[6],poligon4[14],poligon4[15])
    myRenderer.glFillTriangle(poligon4[6],poligon4[11],poligon4[14])
    myRenderer.glFillTriangle(poligon4[6],poligon4[10],poligon4[11])
    myRenderer.glFillTriangle(poligon4[6],poligon4[9],poligon4[10])


    myRenderer.glFillTriangle(poligon4[6],poligon5[1],poligon5[0])
    myRenderer.glFillTriangle(poligon4[6],poligon4[9],poligon5[0])
    myRenderer.glFillTriangle(poligon4[6],poligon4[7],poligon5[1])
    myRenderer.glFillTriangle(poligon4[7],poligon5[1],poligon5[2])
    myRenderer.glFillTriangle(poligon4[7],poligon5[2],poligon5[3])
    myRenderer.glFillTriangle(poligon4[7],poligon4[8],poligon5[3])
    myRenderer.glFillTriangle(poligon4[8],poligon4[9],poligon5[3])
    myRenderer.glFillTriangle(poligon4[9],poligon5[0],poligon5[3])


def drawShrek():

    # myRenderer.glColor(0.4,1,0.5)
    for vert in shrek:
        myRenderer.glVertex(vert.x,vert.y)

    for i in range(len(shrek)-1):
        myRenderer.glLine(shrek[i].x,shrek[i].y,shrek[i+1].x,shrek[i+1].y)

   





def drawPoligon5():
    
    for i in range(len(poligon5)-1):
        myRenderer.glLine(poligon5[i].x,poligon5[i].y,poligon5[i+1].x,poligon5[i+1].y,)




myRenderer = Renderer(windoWidth, windowHeight)
myRenderer.glViewPort(viewportX,viewportY,viewportWidth,viewportHeight)


# myRenderer.glFillTriangle(V2(480,780 ),V2(750,624), V2(850,800))
# myRenderer.glTuple(V2(0,1),V2(2,5))


drawPoligon1()
drawPoligon2()
drawPoligon3()
drawPoligon4()

drawShrek()


myRenderer.glFinish("output.bmp")