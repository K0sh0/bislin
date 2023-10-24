from sympy import symbols, nonlinsolve

# Define symbols
a, b, c, d = symbols('a, b, c, d', real=True)

# Define list of equations
eqs = [a*(-14808.518)+b*(-5526904.965)+c*(3172638.644)+d,
       a*(-14805.950)+b*(-5526897.001)+c*(3172652.442)+d,
       a*(-14803.351)+b*(-5526888.981)+c*(3172666.353)+d]

# Solving for c
c_val = nonlinsolve(eqs,[c]).args[0].args[0]
eqs = [eq.subs(c, c_val) for eq in eqs]

# Solving for d
d_val = nonlinsolve(eqs,[d]).args[0].args[0]
eqs = [eq.subs(d, d_val) for eq in eqs]

# Solving for b
b_val = nonlinsolve(eqs,[b]).args[0].args[0]

# Print the value for b
print('B:', b_val)

# Define list of equations again (original)
eqs = [a*(-14808.518)+b*(-5526904.965)+c*(3172638.644)+d,
       a*(-14805.950)+b*(-5526897.001)+c*(3172652.442)+d,
       a*(-14803.351)+b*(-5526888.981)+c*(3172666.353)+d]

# Solving for b (again)
b_val = nonlinsolve(eqs,[b]).args[0].args[0]
eqs = [eq.subs(b, b_val) for eq in eqs]

# Solving for d (again)
d_val = nonlinsolve(eqs,[d]).args[0].args[0]
eqs = [eq.subs(d, d_val) for eq in eqs]

# Solving for c (again)
c_val = nonlinsolve(eqs,[c]).args[0].args[0]

# Print the value for c
print('C:', c_val)

# Define list of equations again (original)
eqs = [a*(-14808.518)+b*(-5526904.965)+c*(3172638.644)+d,
       a*(-14805.950)+b*(-5526897.001)+c*(3172652.442)+d,
       a*(-14803.351)+b*(-5526888.981)+c*(3172666.353)+d]

# Solving for b (again)
b_val = nonlinsolve(eqs,[b]).args[0].args[0]
eqs = [eq.subs(b, b_val) for eq in eqs]

# Solving for c (again)
c_val = nonlinsolve(eqs,[c]).args[0].args[0]
eqs = [eq.subs(c, c_val) for eq in eqs]

# Solving for d (again)
d_val = nonlinsolve(eqs,[d]).args[0].args[0]

# Print the value for d
print('D:', d_val)

# Formatting and printing the string representation of the equation
str_1 = f"x + {b_val}*y + {c_val}*z + {d_val} = 0"
print(str_1)
