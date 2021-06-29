'''
find_greater_numbers([1,2,3]) # 3 
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
'''

def find_greater_numbers(l):
    greater = 0
    for i, n in enumerate(l):
        for j in range (i + 1, len(l)):
            if l[j] > n:
                greater += 1
    return greater