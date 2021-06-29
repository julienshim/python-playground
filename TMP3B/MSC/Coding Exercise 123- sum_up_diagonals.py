'''
EXAMPLES:


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
 
sum_up_diagonals(list1) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
 
sum_up_diagonals(list2) # 30
 
list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

sum_up_diagonals(list3) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
 
sum_up_diagonals(list4) # 68
'''

def sum_up_diagonals(l):
    f = len(l)
    b = f - 1
    forward = sum(l[i][i] for i in range(f))
    back = sum(l[i][b-i] for i in range(f))
    return forward + back

# instructor solve

# def sum_up_diagonals(arr):
#     total = 0
    
#     for i,val in enumerate(arr):
#         total += arr[i][i]
#         total += arr[i][-1-i]
#     return total