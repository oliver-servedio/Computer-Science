# This is using eval apparently their is another way

equation = input()
assignments = input()

# This has to go first to avoid replacing the a in and
equation = equation.replace(' AND', ' and' )                        # Spacing bc of NAND
equation = equation.replace(' OR', ' or')
equation = equation.replace('NOT', 'not')
equation = equation.replace('XOR', '^')
equation = equation.replace('NAND', '^ False and')                 

values = {v.split('=')[0]: v.split('=')[1] == 'True' for v in assignments.split()}
for var, val in values.items():
    equation = equation.replace(var, str(val))
print(equation)
print(values)


if eval(equation):
    print('Rainy season starts!')
else:
    print('No rain tomorrow.')

# NOT (A NAND B)
# A=True B=True