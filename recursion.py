# ## factorial function using recursion

# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return num * factorial(num-1)
    
# print(factorial(5))

######################################
## calculate sum using recursion

# given_array = [2, 4, 5, 7, 8, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]

# def recusive_sum(arr,sum,i):
#     if i < len(arr):
#         sum += arr[i]
#         return recusive_sum(arr,sum,i+1)
#     else:
#         return sum

# print(recusive_sum(given_array,0,0))

##################################################

## Binary search using recursion

# given_array = [2, 4, 5, 7, 8, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]

# def binarysearch_recursion(arr,target,low,high):
#     if low > high:
#         return False
#     else:
#         mid = (low + high) // 2
#         if target == arr[mid]:
#             return f'{arr[mid]} is found at index {mid}'
#         elif target > arr[mid]:
#             return binarysearch_recursion(arr,target,mid+1,high)
#         else:
#             return binarysearch_recursion(arr,target,low,mid-1)
        
# print(binarysearch_recursion(given_array,27,0,len(given_array)-1))

##################################################

## draw a ruller using recursion

# def draw_line(tick_length, tick_label=''):
#     line = '-' * tick_length
#     if tick_label:
#         line = line + ' ' + tick_label
#     print(line)

# def draw_interval(center_length):
#     if center_length > 0:
#         draw_interval(center_length - 1)
#         draw_line(center_length)
#         draw_interval(center_length - 1)

# def draw_ruler(num_inches,major_length):
#     draw_line(major_length,'0')

#     for i in range(1,num_inches + 1):
#         draw_interval(major_length-1)
#         draw_line(major_length,str(i))

# draw_ruler(10,5)

#############################################

## fibonacci number using recursion

# def fibonacci(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fibonacci(num-1) + fibonacci(num-2)

# print(fibonacci(8))

#################################################
## fibonacci efficient way
# def goodfibonacci(num):
#     if num <= 1:
#         return (num,0)
#     else:
#         (a,b) = goodfibonacci(num-1)
#         print(a,b)
#         return (a+b,a)
    
# print(goodfibonacci(5))

#################################################

## two power
# def twopower(n):
#     if n == 1:
#         return True
#     elif n >= 2:
#         return twopower(n / 2)
#     else:
#         return False
# print(twopower(16))

##################################################
