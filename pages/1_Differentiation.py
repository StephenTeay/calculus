# pages/1_📈_Differentiation.py
import streamlit as st
from sympy import symbols, diff, latex, parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

transformations = (standard_transformations + (implicit_multiplication_application,))

def show_differentiation_page():
    st.set_page_config(page_title="Differentiation", page_icon="📈")
    st.title("📈 Differentiation")
    
    # User input
    function = st.text_input("Enter a function (e.g., x**2 + sin(y)):", "x**2")
    var = st.text_input("Variable to differentiate with respect to:", "x")
    order = st.number_input("Order of derivative", min_value=1, max_value=5, value=1)
    
    try:
        # Parse inputs
        x = symbols(var)
        expr = parse_expr(function, transformations=transformations)
        
        # Compute derivative
        derivative = diff(expr, x, order)
        st.latex(f"\\frac{{d^{order}f}}{{d{var}^{order}}} = {latex(derivative)}")
        
        # Numerical evaluation
        if st.checkbox("Evaluate at a point"):
            point = st.number_input(f"Value of {var}:", value=0.0)
            result = derivative.subs(x, point)
            st.write(f"Result at {var} = {point}: **{result.evalf()}**")
            
    except Exception as e:
        st.error(f"Error: {str(e)}")
if __name__ == "__main__":
    show_differentiation_page()

st.caption("Built with Streamlit & SymPy & Python")