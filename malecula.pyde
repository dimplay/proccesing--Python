def setup():
    size(400,400)
    background(244)
def draw():
    line(200,200,100,100)
    ellipse(100,100,20,20)
    ellipse(200,200,100,100)
def mouseClicked():
    stroke(random(0,255),random(0,233),random(0,244))
    fill(random(0,255),random(0,244),random(0,233))
