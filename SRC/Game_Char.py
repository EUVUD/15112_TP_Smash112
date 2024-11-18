class bullet:
    def __init__(self, name, x, y, size, velocity):
        self.x = x
        self.y = y
        self.size = size
        self.velocity = velocity

class char:
    def __init__(self, name, x, y, size, color, direction, bulletList):
        self.name = name
        self.x = x
        self.y = y
        self.size = size
        self.jump = True
        self.color = color
        self.dy = 0
        self.direction = direction
        self.bulletList = bulletList

    def __repr__(self):
        return f'{self.name} with size {self.size} is at ({self.x},{self.y})'
    
    def shoot(self):
        yPos = self.y + self.size/2
        velocity = None
        if self.direction == 'left':
            xPos = self.x
            velocity = -10
        else:
            xPos = self.x + self.size
            velocity = 10
        newBullet = bullet('bullet', xPos, yPos, 3, velocity)
        self.bulletList.append(newBullet)





