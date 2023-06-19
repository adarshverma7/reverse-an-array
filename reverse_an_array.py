'''
def reverse_array(arr):
    arr.reverse()
    return arr
arr=[13,2,3,"ada"]
reverse_array(arr)
print("new arra=",arr)
'''
#                            OR
def reverse_arr(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start=start+1
        end=end-1
arr=[12,6,4,"asds"]
print(arr)
reverse_arr(arr,0,3)
print(arr)