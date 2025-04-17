# pages/5_Summation.py
import streamlit as st
from sympy import Sum, symbols, latex, oo, parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

transformations = (standard_transformations + (implicit_multiplication_application,))

st.set_page_config(page_title="Summation", page_icon="Σ")
st.title("Summation/Series Σ")

# Inputs
expression = st.text_input("Summation expression (e.g., 1/n**2):", "1/n**2")
sum_var = st.text_input("Summation index:", "n")
lower = st.number_input("Lower bound:", value=1)
upper = st.text_input("Upper bound (use 'oo' for infinity):", "oo")

try:
    n = symbols(sum_var)
    expr = parse_expr(expression, transformations=transformations)
    upper_bound = oo if upper == "oo" else int(upper)
    
    summation = Sum(expr, (n, lower, upper_bound))
    result = summation.doit()
    
    st.latex(f"\\sum_{{ {sum_var} = {lower} }}^{{ {upper} }} {latex(expr)} = {latex(result)}")
    
    # Check convergence for infinite series
    if upper_bound == oo:
        if result.is_finite:
            st.success("Series converges")
        else:
            st.warning("Series diverges")

except Exception as e:
    st.error(f"Error: {str(e)}")


st.caption("Built with Streamlit & SymPy & Python")