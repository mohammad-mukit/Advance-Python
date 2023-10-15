#formating string start

# name = 'Mukit'
# age = 23
# print('Hello, %s your age is %d' % (name,age))


# mylist = ['mukit',2,3]
# print('A list : %s' %mylist)


# total = 20.2345
# print('number is : %.3f' % total )

# print(f'number is  {total:.3f}')

# number = 3.14159
# formatted_string = f"The value of pi is {number:.3f}"
# print(formatted_string)

# formating string end
#######################################################

#string manipulation 

# details = 'Hello this is me'
# print(details[2:9:2])

# print(details[::-1])

# new = details.split(' ')
# reversestring = ' '.join(new[::-1])
# print(reversestring)

###############################################

#reverser string
# given_string = 'Hello this is mukit'

# wordlist = given_string.split()[::-1]
# print(wordlist)
# reverse_string = ' '.join(wordlist)
# print(reverse_string)

####################################

#removing character from string

# given_string = 'Hello123this123is123mukit'
# replace_string = given_string.replace('123',' ')
# print(replace_string)

# translate_string = given_string.translate({ord(i): ' ' for i in '123'})
# print(translate_string)


# remove_first_char = given_string.removeprefix('H')
# remove_last_char = given_string.removesuffix('t')
# print(remove_first_char)
# print(remove_last_char)


#####################################

#count character of a string

# given_string = 'Hello this is mukit'
# count = 0
# for char in given_string:
#     if char == ' ':
#         continue
#     else:
#         count +=1
# print(count)

############################################

#executing python code from a string

# code = '''
# print('Hello this code is string. but can be executed')
# a = 5
# b = 5
# sum = a + b
# print(sum)
# '''
# def execute_code():
#     exec(code)

# execute_code()

#################################################

#code execute from a text file

# with open('stringfile1.txt', 'r') as file:
#     file_read = file.read()

# def execute_file():
#     exec(file_read)

# execute_file()

##################################################