def square_plus_one(a):
    result = a*a+1
    return result
print(square_plus_one(2))

def quadratic(a, b, c):
    x1 = (-b+(b*b-4*a*c)**0.5)/(2*a)
    x2 = (-b-(b*b-4*a*c)**0.5)/(2*a)
    return x1,x2
print(quadratic(1,2,3))

import webbrowser
def BMI(weight,weight_unit,height,height_unit):
    if weight_unit == '2' and height_unit == '2':
        bmi = 703*weight/height**2
    elif weight_unit == '1' and height_unit == '1':
        bmi = weight/height**2
    elif weight_unit == '2':
        weight = 0.453592*weight
        bmi = weight/height**2
    elif height_unit == '2':
        height = 0.0254*height
        bmi = weight/height**2
    else:
        return 'You probably enter invalid information.'
    if bmi < 18.5:
        webbrowser.open('www.mcdonalds.com/us/en-us.html')
        return 'Your bmi is {:2f}. You are underweight.'.format(bmi)
    elif bmi >= 18.5 and bmi < 25:
        return 'Your bmi is {:2f}. You are normal weight.'.format(bmi)
    elif bmi >= 25 and bmi <30:
        return 'Your bmi is {:2f}. You are overweight.'.format(bmi)
    else:
        return 'Your bmi is {:2f}. You are obese.'.format(bmi)

# weight = input('What is your weight?')
# weight_unit = input("Is it in 1:'kg' or 2:'lb'?")
# height = input('What is your height?')
# height_unit = input("Is it in 1:'m' or 2:'in'?")
# print(BMI(float(weight),weight_unit,float(height),height_unit))

import time
time.sleep(1)

def fab(n):
    # this function will return the nth Fabonacci number.
    if n == 1 or n ==2:
        return 1
    else:
        return fab(n-1) + fab(n-2)

print(fab(1))
print(fab(3))

sum = 0
for i in range(1,101):
    sum = sum + i**2
print(sum)

name = input('what is your name?')
value = 0
for i in name:
    if ord(i) in range(65,91):
        value = value + ord(i)-64
    elif ord(i) in range(97,123):
        value = value + ord(i)-96
    else:
        print('You probably enter something invalid.')

print(value)
