print('> Title: Simple Calculator')
print('> Choose an operation:')

print('> 1. Addition')
print('> 2. Subtraction')
print('> 3. Multiplication')
print('> 4. Division')

choice = int(input('> Enter Selection: '))

number_1 = int(input('> Provide the first number: '))
number_2 = int(input('> Provide the second number: '))

if choice == 1:
    print('The answer is:', number_1 + number_2)
if choice == 2:
    print('The answer is:', number_1 - number_2)
if choice == 3:
    print('The answer is:', number_1 * number_2)
if choice == 4:
    print('The answer is:', number_1 / number_2)