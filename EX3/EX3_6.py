#Asal Kermanpour- Elecrical Engineering student in Kharazmi university- 4012061035
def face(INTLIST):
    '''
(int) -> str
'''
    invertal = max(INTLIST) - min(INTLIST)
    face = " "
    for num in INTLIST:
        if num == invertal:
            face = ":)"
        else:
            face = ":("
    return face
