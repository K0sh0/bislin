import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import time
from sympy import symbols, init_printing, nonlinsolve

# setup variables
a, b, c, d = symbols('a,b,c,d', real=True)
init_printing(use_unicode=True)

# setup google spreadsheet access
scope = ['https://spreadsheets.google.com/feeds', 
         'https://www.googleapis.com/auth/drive',
         'https://www.googleapis.com/auth/drive.file', 
         'https://www.googleapis.com/auth/spreadsheets']

creds = ServiceAccountCredentials.from_json_keyfile_name('mod.json', scope)
client = gspread.authorize(creds)

sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1jftuY0Z9JVNdOj7594mcRu97v79O8wIFrLrqKiiEJxk/edit#gid=0").sheet1

planes = []

for i in range(0, 10, 3):
    # read and symbolize variables from spreadsheet
    vars = []
    for j in range(i, i + 3):
        val = str(j + 2)
        x, y, z = (symbols(sheet.cell(val, col).value) for col in range(8, 11))
        vars.append([x, y, z])

    eqs = [a*x+b*y+c*z+d for x, y, z in vars]
    print("check 1")

    for coef, var in ((c, 'C'), (d, 'D'), (b, 'B')):
        solution = nonlinsolve(eqs, coef).args[0].args[0]
        eqs = [eq.subs([(coef, solution)]) for eq in eqs]
        print(f'{var}: {solution}')

    str_eqs = ' + '.join([f'{coef}/{a}*{var}' for coef, var in zip(eqs[0].args, 'xyz')] + [f'-{eqs[0].args[-1]/a} = 0']
    print(str_eqs)
    planes.append(str_eqs)

# output to csv
pd.DataFrame(planes).to_csv('planes.csv')
