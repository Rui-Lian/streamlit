import streamlit as st

# page config and title
st.set_page_config(page_title="My App", layout="wide")
st.title("APP main title: Hello Streamlit!")

# Create two columns in main page
col1, col2, col3 = st.columns(3)

with col1: 
    # The beginning text, formula
    st.header("column 1 title: Wrods")
    st.write("This is a simple Streamlit app.")
    st.text("Plain text")
    st.markdown("**Markdown** support")
    st.latex(r"\sum_{i = 1}^{n}")

with col2: 
    # Widgets return values directly
    st.header("column 2 title: FUnction")
    name = st.text_input("What's your name?")
    st.write(f"Hello, {name}!")
    # Age slider
    age = st.slider("Your Age", 0, 100)
    st.write(f"You are {age} years old.")

with col3: 
    # Plot a plot
    st.header("column 3 title: plot")
    st.subheader("Plotting a plot")

    import matplotlib.pyplot as plt
    import numpy as np

    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    st.pyplot(fig)


# st.sidebar.widget_name set widgets in sidebar
st.sidebar.header("Settings")
st.sidebar.write("Set the options")
st.sidebar.slider("Select a value", 0, 100)
st.sidebar.text_input("Enter some text")
st.sidebar.button("click me")
st.sidebar.file_uploader("Upload a file")
st.sidebar.checkbox("Check me")
st.sidebar.selectbox("Pick an option", ["A", "B", "C"])



