import streamlit as st 

def hello_world():
    return "Olá, testando"

def main():
    st.write(hello_world())
    
if __name__ == "__main__":
    main()