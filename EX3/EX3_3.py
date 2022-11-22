#Asal Kermanpour- Elecrical Engineering student in Kharazmi University- 4012061035
def Direction(direction):
    """
(list) -> bool
in this function, you will give a destination to a robot to move.
"""
    a = [0, 0]
    for direct in direction:
        if direct == 'n':
            a[0] += 1
        elif direct == 's':
            a[0] -= 1
        elif direct == 'e':
            a[1] += 1
        elif direct == 'w':
            a[1] -= 1
    return a


def Robotpath(direction):
    robot_defult = [ ["e", "n", "e", "e", "n"], ["w", "n", "w", "n", "w", "w", "n"] ]
    dis_location1 = Direction(robot_defult[0])
    dis_location2 = Direction(robot_defult[0])
    arbitary = Direction(direction)
    if arbitary == dis_location1 or arbitary == dis_location2:
        return True
    else:
        return False

Robotpath(['e', 'e', 'n', 'w', 'n'])
        
