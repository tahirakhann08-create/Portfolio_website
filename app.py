import streamlit as st

# Page setup
st.set_page_config(page_title="Tahira Khan | Portfolio", page_icon="🎓", layout="centered")

# Header Section
st.title("👋 Hi, I'm Tahira Khan")
st.subheader("ICS Student | Aspiring Computer Science Student")
st.write("Welcome to my personal portfolio! I am passionate about programming, problem-solving, and technology.")

st.divider()

# About Me
st.header("📌 About Me")
st.write("""
- 🎓 Currently studying **ICS (Intermediate in Computer Science)** under Federal Board.
- 🎯 Strong foundation in Physics, Mathematics, and Computer Science.
- 💡 Interested in software development, data analysis, and building practical projects.
""")

st.divider()

# Skills Section
st.header("🛠️ Skills")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Programming & Tech:**")
    st.write("- Python (Basic/Intermediate)")
    st.write("- HTML & CSS basics")
    st.write("- Problem Solving")

with col2:
    st.markdown("**Core Subjects:**")
    st.write("- Computer Science Concepts")
    st.write("- Mathematics & Logic")
    st.write("- Physics Fundamentals")

st.divider()

# Projects Section
st.header("🚀 Projects")
st.subheader("1. Personal Interactive Portfolio")
st.write("Built an interactive web portfolio using Python and Streamlit to showcase skills, academic profile, and achievements.")

st.divider()

# Contact Form
st.header("📬 Get in Touch")
name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

if st.button("Send Message"):
    if name and email and message:
        st.success(f"Thank you {name}! Your message has been recorded.")
    else:
        st.warning("Please fill out all fields.")
