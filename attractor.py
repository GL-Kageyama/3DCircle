class Attractor(object):
    
    def __init__(self):
        self.position = PVector(0, 0)
        self.mass = 30
        self.g = 0.6;
        
    def attract(self, m):
        force = PVector.sub(self.position, m.position)
        d = force.mag()
        d = constrain(d, 5.0, 25.0)
        
        force.normalize();
        strength = (self.g * self.mass * m.mass) / float(d * d)
        force.mult(strength)
        
        return force
    
    def display(self):
        stroke(239, 245, 144, 100)
        noFill()
        pushMatrix()
        translate(self.position.x, self.position.y, self.position.z)
        sphere(self.mass*8)
        popMatrix()
        
