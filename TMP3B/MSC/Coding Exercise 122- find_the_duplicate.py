'''
find_the_duplicate([1,2,1,4,3,12]) # 1
find_the_duplicate([6,1,9,5,3,4,9]) # 9
find_the_duplicate([2,1,3,4]) # None
'''

def find_the_duplicate(arr):
    for i in range(len(arr)):
        if arr.count(arr[i]) > 1:
            return arr[i]