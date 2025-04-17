# pages/8_Plotting.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sympy import parse_expr, symbols, lambdify
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

transformations = (standard_transformations + (implicit_multiplication_application,))

st.set_page_config(page_title="Plotting", page_icon="📊")
st.title("Plotting 📊")


# Inputs
function_input = st.text_input("Function(s) to plot (comma-separated):", "sin(x), cos(x)")
var = st.text_input("Variable:", "x")
x_min = st.number_input("x-axis min:", value=-5.0)
x_max = st.number_input("x-axis max:", value=5.0)

try:
    x = symbols(var)
    func_strings = function_input.split(",")
    
    # Generate plot
    fig, ax = plt.subplots()
    x_vals = np.linspace(x_min, x_max, 400)
    
    for func_str in func_strings:
        expr = parse_expr(func_str.strip(), transformations=transformations)
        f = lambdify(x, expr, "numpy")
        y_vals = f(x_vals)
        ax.plot(x_vals, y_vals, label=func_str.strip())
    
    ax.set_xlabel(var)
    ax.legend()
    st.pyplot(fig)

except Exception as e:
    st.error(f"Error: {str(e)}")

st.caption("Built with Streamlit & SymPy & Python")