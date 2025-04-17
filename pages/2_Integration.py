# pages/2_∫_Integration.py
import streamlit as st
from sympy import integrate, symbols, latex, oo, parse_expr

def show_integration_page():
    st.set_page_config(page_title="Integration", page_icon="👨‍🔬")
    st.title("∫ Integration")
    
    # User input
    function = st.text_input("Enter a function:", "exp(-x)")
    var = st.text_input("Integration variable:", "x")
    integral_type = st.radio("Integral type", ["Indefinite", "Definite"])
    
    try:
        x = symbols(var)
        expr = parse_expr(function)
        
        if integral_type == "Indefinite":
            result = integrate(expr, x)
            st.latex(f"\\int {latex(expr)} \, d{var} = {latex(result)} + C")
        else:
            lower = st.number_input("Lower bound:", value=0.0)
            upper = st.number_input("Upper bound:", value=0.0)
            result = integrate(expr, (x, lower, upper))
            st.latex(f"\\int_{{{lower}}}^{{{upper}}} {latex(expr)} \, d{var} = {latex(result)}")
            
    except Exception as e:
        st.error(f"Error: {str(e)}")
# To run this page, use the command:
if __name__ == "__main__":
    show_integration_page()

st.caption("Built with Streamlit & SymPy & Python")