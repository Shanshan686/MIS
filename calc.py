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

# Exercise 01-1-1. The volume of a sphere with radius r is (4/3)pi*r^3. What is the volume of sphere with radius 5?
import math
pi = math.pi
r = 5
V = (4/3)*pi*(r^3)
print('The volume of a sphere with radius 5 is {:.2f} cubic units.'.format(V))
# 01-1-2.
price = 24.95
discount = 0.4
ship1 = 3
ship_next = 0.75
copies_60 = price*discount*60+ship1+ship_next*59
print('The total wholesale cost for 60 copies is ${:.2f}.'.format(copies_60))
# 01-1-3.
h_leave = 6
m_leave = 52
easy_m = 8
easy_s = 15
tempo_m = 7
tempo_s = 12
Easy_m = 2*easy_m
Easy_s = 2*easy_s
Tempo_m = 3*tempo_m
Tempo_s = 3*tempo_s
s_back = Easy_s+Tempo_s

m_back = m_leave+Easy_m+Tempo_m+s_back//60
s_back = s_back-(s_back//60)*60

h_back = h_leave+(m_back//60)
m_back = m_back-(m_back//60)*60

print('I get home for breakfast at {:02d}:{:02d}:{:02d} am.'.format(h_back,m_back,s_back))
# 01-1-4.
increase_perc = (89-82)/82
print('The percentage of the increase is {:02.2%}.'.format(increase_perc))
