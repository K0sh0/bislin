from sympy import symbols, nonlinsolve, Eq

def solve_for_symbol(eq_list, symbol_to_solve):
    """
    Function to solve an equation list for a specific symbol
    """
    # Iterate over equation set to implement substitution
    for i in range(0, len(eq_list)):
        # If symbol we're currently solving for has already been replaced, skip
        if symbol_to_solve not in eq_list[i].free_symbols:
            continue

        # Solve for symbol
        _solution = nonlinsolve(eq_list, [symbol_to_solve])
        solution = _solution.args[0].args[0]

        # Replace symbol in all equations
        eq_list = [eq.subs(symbol_to_solve, solution) for eq in eq_list]
        
        print(f'---{symbol_to_solve}: {solution}')

    return eq_list, solution

# Define your system of equations
a, b, c, d, x, y, z = symbols('a b c d x y z', real=True)
init_system = [
    a*(2)+b*(1)+c*(1)+d,
    a*(-1)+b*(2)+c*(1)+d,
    a*(1)+b*(0)+c*(2)+d
]

# Solve for each symbol
init_system, a_solution = solve_for_symbol(init_system, a)
init_system, b_solution = solve_for_symbol(init_system, b)
init_system, c_solution = solve_for_symbol(init_system, c)
