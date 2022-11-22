#Asal Kermanpour- Elecrtical Engineering student in Kharazmi University- 4012061035
def Maxadjacant(list_num):
    '''
(list) -> int
in this function, you will recieve the max of the multipying of your list
'''
    result = []

    for a in range(len(list_num)-1):
        product = list[a] * list[a+1]
        result.append(product)
    MAX = max(result)
    return MAX

