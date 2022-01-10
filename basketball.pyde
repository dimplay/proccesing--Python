x=160
def setup():
    size(400,400)
def draw():
    background(1)
    global x
    strokeWeight(1)
    ellipse(220,240,100,100)
    rect(220-30,240+50,60,60)
    rect(220-30,240+50+60,30,30)
    rect(220-30+30,240+50+60,30,30)
    rect(220-30-20,240+50,20,20)
    rect(210,80,80,40)
    strokeWeight(40)
    stroke(22,40,255)
    point(x,240+50)
    x-=1
    strokeWeight(1)
    ellipse(20,300,60,60)
    stroke(random(0,255),random(0,244),255)
    strokeWeight(10)
    point(random(0,400),random(0,400))
    
    


    
