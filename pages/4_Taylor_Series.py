# pages/4_Taylor_Series.py
import streamlit as st
from sympy import symbols, series, latex, parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

transformations = (standard_transformations + (implicit_multiplication_application,))

st.set_page_config(page_title="Taylor Series", page_icon="∞")
st.title("Taylor Series Expansion ∞")

# Inputs
function = st.text_input("Function to expand (e.g., cos(x)):", "exp(x)")
var = st.text_input("Variable:", "x")
expansion_point = st.number_input("Expansion point:", value=0.0)
degree = st.number_input("Degree of expansion:", min_value=1, max_value=10, value=5)

try:
    x = symbols(var)
    expr = parse_expr(function, transformations=transformations)
    
    # Generate Taylor series
    taylor_expr = series(expr, x, expansion_point, degree + 1).removeO()
    st.latex(f"\\text{{Taylor expansion of }} {latex(expr)} \\text{{ at }} {var} = {expansion_point}:")
    st.latex(f"{latex(taylor_expr)} + \\mathcal{{O}}({var}^{degree + 1})")

except Exception as e:
    st.error(f"Error: {str(e)}")

st.caption("Built with Streamlit & SymPy & Python")