# ## factorial function using recursion

# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return num * factorial(num-1)

# print(factorial(5))

######################################
# calculate sum using recursion

# given_array = [2, 4, 5, 7, 8, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]

# def recusive_sum(arr,sum,i):
#     if i < len(arr):
#         sum += arr[i]
#         return recusive_sum(arr,sum,i+1)
#     else:
#         return sum

# print(recusive_sum(given_array,0,0))

##################################################

# Binary search using recursion

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

# draw a ruller using recursion

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

# fibonacci number using recursion

# def fibonacci(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fibonacci(num-1) + fibonacci(num-2)

# print(fibonacci(4))

#################################################
# fibonacci efficient way
# def goodfibonacci(num):
#     if num <= 1:
#         return (num,0)
#     else:
#         (a,b) = goodfibonacci(num-1)
#         return (a+b,a)
# print(goodfibonacci(6))

#################################################

# two power
# def twopower(n):
#     if n == 1:
#         return True
#     elif n >= 2:
#         return twopower(n / 2)
#     else:
#         return False
# print(twopower(16))

##################################################
# recursion for reversing an array

# given_array = [2,3,4,6,7,9,8,10]

# def reversearray(arr,start,end):

#     if start < end-1:
#         arr[start],arr[end - 1] = arr[end-1],arr[start]
#         reversearray(arr,start+1,end-1)
#     return arr

# print(reversearray(given_array,0,len(given_array)))
#######################################################
# important lesson dsa in python book page 172-173
# calculate power using recursion

# def power(base,p):
#     if p == 0:
#         return 1
#     else:
#         partial = power(base, p // 2)
#         result = partial * partial
#         if p % 2 == 1:
#             result *= base
#         return result

# print(power(2,3))

#############################################################

# power of three
# def threepower(n):
#     if n <= 0:
#         return False
#     if n == 1:
#         return True
#     else:
#         result = threepower(n / 3)
#         if result & result == True:
#             return True
#         else:
#             return False

# print(threepower(6))

############################################################
# another approach of calculating power of any number
# example for number 4. this is efficient from above solution
# def power(n):
#     if n == 1 or n == 4:
#         return True
#     if n > 4 and n % 4 == 0:
#         return power(n / 4)
#     return False
# print(power(16))

############################################################
# calcutlating sum of an array using binary recursion

# given_array = [2,4,6,7,8,9,2,3,6,5]

# def binaryrecursum(arr,start,end):
#     if start >= end:
#         return 0
#     elif start == end-1:
#         return arr[start]
#     else:
#         mid = (start + end)//2
#         return binaryrecursum(arr,start,mid) + binaryrecursum(arr,mid,end)

# print(binaryrecursum(given_array,0,len(given_array)))

##############################################################
# all permutation using multiple recursion

k = 3
s = ''
u = {'a','b','c'}
puzzle = 'acb'

def allpermutation(k,s,u):
    for item in u:
        s += item
        u.remove(item)
        if k == 1:
            return s
        else:
            allpermutation(k-1,s,u)
        s = s.removesuffix(item)
        u.add(item)
        
allpermutation(k,s,u)
