#Asal Kermanpour- Electrical Engineering in Kharazmi university- 4012061035

def position(column, line):
    map = { "a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8 }
    character_map = []
    character_map.append(map[column])
    character_map.appernd(line)
    return character_map

def bishop(characterlist):
    possible = []
    i = characterlist[0]
    j = characterlist[1]
    while i+2<=7 and j+1<=7:
        possible.append([i+2, j+1])
    while i-2>1 and j+1<=7:
        possible.append([i-2, j+1])
    while x<=7 and y>1:
        x += 1
        y -= 1
        possible.append([x, y])
    return possible

#استاد شرمنده ناقص حل شده است چون راه حلي به ذهنم نميرسيد
