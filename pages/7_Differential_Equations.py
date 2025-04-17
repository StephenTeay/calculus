# pages/7_Differential_Equations.py
import streamlit as st
from sympy import symbols, Function, dsolve, latex, Eq
from sympy.parsing.sympy_parser import parse_expr

st.set_page_config(page_title="Differential Equations", page_icon="🧮")
st.title("Differential Equations 🧮")

# Inputs
ode_input = st.text_input("ODE (e.g., y'' + y = 0):", "y'' + y")
dep_var = st.text_input("Dependent variable:", "y")
indep_var = st.text_input("Independent variable:", "x")

try:
    x = symbols(indep_var)
    y = Function(dep_var)(x)
    
    # Parse ODE
    ode = parse_expr(ode_input.replace(f"{dep_var}''", f"Derivative({dep_var}(x), (x, 2))"))
    solution = dsolve(ode, y)
    
    st.latex(f"\\text{{Solution}}:")
    st.latex(latex(solution))

except Exception as e:
    st.error(f"Error: {str(e)}")


st.caption("Built with Streamlit & SymPy & Python")