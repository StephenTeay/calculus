# pages/6_Equation_Solving.py
import streamlit as st
from sympy import symbols, solve, latex, Eq
from sympy.parsing.sympy_parser import parse_expr

st.set_page_config(page_title="Equation Solving", page_icon="⚖️")
st.title("Equation Solving ⚖️")

# Inputs
equation_input = st.text_input("Equation(s) (comma-separated):", "x**2 - 4")
variables = st.text_input("Variables to solve for (comma-separated):", "x")

try:
    # Parse equations
    eq_strings = equation_input.split(",")
    equations = [parse_expr(eq.strip()) for eq in eq_strings]
    
    # Parse variables
    vars = [symbols(v.strip()) for v in variables.split(",")]
    
    # Solve
    solutions = solve(equations, vars)
    
    if not solutions:
        st.write("No solutions found.")
    else:
        st.latex("\\text{Solutions}:")
        for sol in solutions:
            st.latex(latex(sol))

except Exception as e:
    st.error(f"Error: {str(e)}")

st.caption("Built with Streamlit & SymPy & Python")