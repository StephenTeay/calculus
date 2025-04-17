# app.py
import streamlit as st

st.sidebar.title("Calculus Toolbox")
st.sidebar.markdown("Select a page from the sidebar.")






st.sidebar.markdown("---")
st.sidebar.caption("Built with Streamlit & SymPy")
# pages/9_Documentation.py
import streamlit as st
from streamlit.components.v1 import html

def doc_page():
    st.title("📖 Documentation Guide")
    st.markdown("""
    <style>
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .fade-in {
            animation: fadeIn 1s ease-in;
        }
        .highlight {
            background-color: #fffdba;
            padding: 8px;
            border-radius: 4px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 1em 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
    </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="fade-in">', unsafe_allow_html=True)
        st.header("📚 Symbol Reference Table")
        st.markdown("""
        | Mathematical Symbol | App Input          | Examples                     |
        |---------------------|--------------------|------------------------------|
        | Exponentiation      | `**`               | `x**2` for x²                |
        | Square Root         | `sqrt()`           | `sqrt(x)` for √x             |
        | Trigonometric       | `sin()`, `cos()`   | `sin(pi/2)` for sin(π/2)     |
        | Exponential         | `exp()`            | `exp(2)` for e²              |
        | Natural Log         | `log()`            | `log(10)` for ln(10)         |
        | Infinity            | `oo`               | `x -> oo` for x→∞           |
        | Derivative          | `diff()`           | `diff(x**2, x)` for d/dx(x²)|
        """)

        st.markdown("</div>", unsafe_allow_html=True)

    with st.expander("🚀 Input Formatting Guide", expanded=True):
        st.markdown("""
        **Common Patterns:**
        ```python
        # Basic operations
        2*x + 3/y - 4**z
        
        # Trigonometric functions
        sin(2*pi*x) + cos(theta)**2
        
        # Complex expressions
        exp(-x**2)/(sqrt(2*pi))
        ```
        """)

    with st.expander("⚠️ Common Errors & Solutions"):
        error_table = """
        | Error Type         | Cause                      | Solution                     |
        |--------------------|----------------------------|------------------------------|
        | SyntaxError        | Missing operators          | Use `2*x` instead of `2x`    |
        | NameError          | Undefined symbols          | Define variables first       |
        | NotImplementedError| Complex operations         | Simplify input               |
        | ValueError         | Invalid bounds             | Check numeric limits         |
        """
        st.markdown(error_table)

    with st.expander("📈 Page-Specific Guides"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Differentiation**
            - Use `x**3` for x³
            - Partial derivatives: `diff(x*y, x)`
            
            **Integration**
            - Definite: `(x, 0, 5)`
            - Improper: `(x, 0, oo)`
            """)

        with col2:
            st.markdown("""
            **Taylor Series**
            - Point: 0 for Maclaurin
            - Degree = Terms-1
            
            **Differential Equations**
            - Use `y''` for second derivatives
            - Initial conditions optional
            """)

    st.markdown("""
    <script>
    // Simple animation for headers
    document.querySelectorAll('h2, h3').forEach((el) => {
        el.style.transition = 'all 0.3s ease';
        el.onmouseover = () => {
            el.style.color = '#FF4B4B';
            el.style.transform = 'translateX(10px)';
        }
        el.onmouseout = () => {
            el.style.color = '';
            el.style.transform = '';
        }
    });
    </script>
    """, unsafe_allow_html=True)

doc_page()
st.caption("Built with Streamlit & SymPy & Python")