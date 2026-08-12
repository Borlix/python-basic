# __init__ Function -
# All classes have a function call __init__() , which is always executed when object is bing called

class home :
    def __init__(self):
        pass                                 # Default Constructor

    def __init__(self, color , floor):       # Parameterized Constructor
        self.color = color
        self.floor = floor

hm1 = home("Green", 4)
print(hm1.color, hm1.floor)

hm2 = home("Yellow", 3)
print(hm2.color , hm2.floor)
