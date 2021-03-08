'''
remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 
'''

def remove_every_other(arr):
    return arr[::2]

# alternative

# def remove_every_other(lst):
#     return [val for i,val in enumerate(lst) if i % 2 == 0]