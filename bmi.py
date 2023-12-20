def input_height():
    input_cm = input('Please input your height here in cm: ')
    if '.' in input_cm:
        return(float(input_cm))
    else:
        return(int(input_cm))

def input_weight():
    iput_kg = input('Please input your weight here in kg: ')
    if '.' in iput_kg:
        return(float(iput_kg))
    else:
        return(int(iput_kg))



def bmi_check(height_cm,weight_kg):
    height_m = (height_cm/100)
    bmi = round((weight_kg/(height_m**2)))
    if bmi < 16:
        print(f'{bmi:}: Severe Thinness')
    elif 16 <= bmi < 17:
        print(f'{bmi:}: Moderate Thinness')
    elif 17 <= bmi < 18.5:
        print(f'{bmi:}: Mild Thinness')
    elif 18.5 <= bmi < 25:
        print(f'{bmi:}: Normal')
    elif 25 <= bmi < 30:
        print(f'{bmi:}: Overweight')
    elif 30 <= bmi < 35:
        print(f'{bmi:}: Obese Class I')
    elif 35 <= bmi < 40:
        print(f'{bmi:}: Obese Class II')
    else:
        print(f'{bmi:}: Obese Class III')

height_cm = input_height()

weight_kg = input_weight()

bmi_check(height_cm,weight_kg)