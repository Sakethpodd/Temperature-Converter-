
def convert_temperature(value, input_choice, output_choice):
    if input_choice == 'C':
        if output_choice == 'F':
            return value * 1.8 + 32
        elif output_choice == 'K':
            return value + 273.15
        else:
            return value
    elif input_choice == 'F':
        if output_choice == 'C':
            return (value - 32) / 1.8
        elif output_choice == 'K':
            return (value + 459.67) * 5 / 9
        else:
            return value
    elif input_choice == 'K':
        if output_choice == 'C':
            return value - 273.15
        elif output_choice == 'F':
            return value * 9 / 5 - 459.67
        else:
            return value
    else:
        return value

while True:
    print('Enter the input temperature value:')
    value = float(input())
    
    print('Enter the input temperature scale (C, F, K):')
    input_choice = input().upper()
    
    print('Enter the output temperature scale (C, F, K):')
    output_choice = input().upper()
    
    result = convert_temperature(value, input_choice, output_choice)
    print(f'{value} {input_choice} = {result} {output_choice}')
    
    print('Enter q to quit, or any other key to continue:')
    choice = input().lower()
    if choice == 'q':
        break


