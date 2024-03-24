class Coordinates:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    #GETTERS
    def get_x(self):
        return self.__x
    def set_x(self, x):
        self.__x = x
    
    #SETTERS
    def get_y(self):
        return self.__y
    def set_y(self, y):
        self.__y = y

#POSITION INHERITS PROPERTIES FROM COORDINATES
class Position(Coordinates):
    def __init__(self, x, y, dir):
        super().__init__(x, y)
        self.__dir = dir
    
    #GETTER AND SETTER
    def get_dir(self):
        return self.__dir
    def set_dir(self, dir):
        self.__dir = dir

#FUNCTION TO TURN THE ROBOT
def turn(curr_dir, command):
    if (curr_dir == "N"):
        curr_dir = "W" if command=="L" else "E"
    elif (curr_dir == "S"):
        curr_dir = "E" if command=="L" else "W"
    elif (curr_dir == "W"):
        curr_dir = "S" if command=="L" else "N"
    elif (curr_dir == "E"):
        curr_dir = "N" if command=="L" else "S"
    return curr_dir

#FUNCTION TO CHECK IF THE INSTRUCTIONS CONFINES THE ROBOT WITHIN BOUNDARY
def within_boundary(upper_right_coordinates, curr_x, curr_y, dir, instructions):
    max_x = upper_right_coordinates.get_x()
    max_y = upper_right_coordinates.get_y()
    
    for i in instructions:
        if (i == "L" or i == "R"):
            dir = turn(dir, i)
        else:
            if (dir == "N"):
                curr_y+=1
            elif (dir == "S"):
                curr_y-=1
            elif (dir == "E"):
                curr_x+=1
            elif (dir == "W"):
                curr_x-=1
        
        if (curr_x>max_x or curr_x<0 or curr_y>max_y or curr_y<0):
            return False
    return True

#FUNCTION TO MOVE THE ROBOT ACCORDING TO THE GIVEN INSTRUCTIONS
def move(upper_right_coordinates, curr_position, instructions):
    #FIRST CHECKS IF THE INSTRUCTIONS ARE VALID
    if not within_boundary(upper_right_coordinates, curr_position.get_x(), curr_position.get_y(), curr_position.get_dir(), instructions):
        return f"{curr_position.get_x()} {curr_position.get_y()} {curr_position.get_dir()}"

    for i in instructions:
        if (i == "L" or i == "R"):
            curr_position.set_dir(turn(curr_position.get_dir(), i))
        else:
            curr_dir = curr_position.get_dir()
            if (curr_dir == "N"):
                curr_position.set_y(curr_position.get_y()+1)
            elif (curr_dir == "S"):
                curr_position.set_y(curr_position.get_y()-1)
            elif (curr_dir == "E"):
                curr_position.set_x(curr_position.get_x()+1)
            elif (curr_dir == "W"):
                curr_position.set_x(curr_position.get_x()-1)
    return f"{curr_position.get_x()} {curr_position.get_y()} {curr_position.get_dir()}"

#PLS UNCOMMENT THE BELOW CODE FOR GIVING CUSTOM INPUT

'''user_input = input("Enter upper right coordinates: ")
initial_pos = input("Enter initial position and heading direction: ")
instructions = input("Enter instruction string: ")

[x, y] = user_input.split()
max_x = int(x) 
max_y = int(y)

[xi, yi, dir] = initial_pos.split()
initial_x = int(xi)
initial_y = int(yi)

upper_right_coordinates = Coordinates(max_x, max_y)
position = Position(initial_x, initial_y, dir)

print(move(upper_right_coordinates, position, instructions)) '''



