def render(st):
    st.markdown("""
        <style>
            .button {
                display: inline-block;
                padding: 10px 20px;
                font-size: 16px;
                font-weight: bold;
                color: #262626 !important;
                background-color: gainsboro;
                border: none;
                border-radius: 5px;
                text-align: center;
                text-decoration: none !important;
                cursor: pointer;
            }
            .button:hover {
                background-color: azure;
            }
            
            .fill-container {
                display: block !important;
                width: 100% !important;
                text-align: center !important;
                padding: 15px;
            }

        </style>
    """, unsafe_allow_html=True)
