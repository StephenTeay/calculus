# pages/3_🔍_Limits.py
import streamlit as st
from sympy import limit, Symbol, latex, parse_expr,oo
from sympy.parsing.sympy_parser import parse_expr

def show_limits_page():
    st.set_page_config(page_title="Limits", page_icon="🔍")
    st.title("🔍 Limits")
    
    function = st.text_input("Function (e.g., sin(x)/x):", "sin(x)/x")
    var = st.text_input("Variable approaching a value:", "x")
    target = st.text_input("Target value (e.g., 0, oo):", "oo")
    
    try:
        x = Symbol(var)
        expr = parse_expr(function)
        if target != "oo":
            t = parse_expr(target) 
        else:
            t == parse_expr("oo")
        
        result = limit(expr, x, t)
     
        st.latex(f"\\lim_{{{var} \\to {target}}} {latex(expr)} = {latex(result)}")
        
    except Exception as e:
        st.error(f"Limit does not exist or could not be computed: {str(e)}")

if __name__ == "__main__":
    show_limits_page()


st.caption("Built with Streamlit & SymPy & Python")