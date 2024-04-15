class Cylinder:

    pi = 3.14
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.height * (self.radius)**2 * Cylinder.pi
    
    def surface_area(self):
        top = Cylinder.pi*(self.radius**2)
        return 2*top + (2*self.height * self.radius * Cylinder.pi)

a= int(input("Enter a height of the cylinder: "))
b= input(" What variable do you have? Enter d for diameter or r for radius: ")
while b:
    if b == "d":
         b = (int(input("Enter a diameter of the cylinder: ")))/2
         break
    elif b == 'r':
        b = int(input("Enter a radius of the cylinder: "))
        break
    elif b == " ":
        b = input(" Please, enter d for diameter or r for radius: ")
        
    else :
        print ("Wrong variable")
        b = " "
        
               
my_Cylinder = Cylinder(a, b)


v = my_Cylinder.volume()
s = my_Cylinder.surface_area()

print('V='+ str(v))
print('S='+ str(s))
