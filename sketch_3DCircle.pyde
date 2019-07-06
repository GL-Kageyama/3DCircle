from attractor import Attractor
from mover import Mover

max_movers = 150
angle = 0

a = Attractor()

def setup():
    size(800, 800, P3D)
    background(255)
    
    global movers
    movers = [Mover(random(0.01, 8), random(-width/2, width/2), \
                    random(-height/2, height/2), random(-150, 150)) \
                    for i in xrange(max_movers) ]
    
def draw():
    global angle, a
    background(98, 54, 40)
    sphereDetail(40)
    lights()
    translate(width/2, height/2)
    
    rotateY(angle)
    
    a.display()
    
    for mover in movers:
        force = a.attract(mover)
        mover.applyForce(force)
        mover.update()
        mover.display()
        
    angle += 0.01
                     
    
    
    
