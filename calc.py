# print((3+15+2+43)*2019)
#
# n=100
# n+= 1
# print(n)

# first_name = 'Shanshan'
# last_name = 'Yang'
# print(first_name+' '+last_name)
#
# print((first_name+' ')*4)
# print('hello, {}'.format(last_name))
# print('hello, {}. You are {} year old.'.format(first_name,20))
#
# template = 'hello, {}! You are {} years old.'
# name1 = 'Grace'
# age1 = 20
# name2 = 'Aida'
# age2 = 32
# print(template.format(name1,age1))
# print(template.format(name2,age2))
#
# print('Pi equals {:.2f}'.format(3.1415926))
#
# template = 'hello, {name}! You are {age} years old.'
# print(template.format(age=age1,name=name1))

# Exercise2-1.How many seconds are there in 42 minutes 42 seconds
print('There are {} seconds.'.format(42*60+42))
# 2-2.How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
print('There are {:.2f} miles.'.format(10/1.61))
# 2-3.If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in mimutes and seconds)?
time_second = 42*60+42
length_mile = 10/1.61
print('Your average pace is {:.2f} seconds per mile.'.format(time_second/length_mile))
