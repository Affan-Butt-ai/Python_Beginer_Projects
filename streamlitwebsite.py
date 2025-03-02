import streamlit as st
import random
import time

st.title("The Random Inspiration Generator")

# List of inspirational quotes, ideas, and prompts
inspirations = [
    "Write a short story about a robot who learns to paint.",
    "Try a new recipe from a cuisine you've never explored.",
    "Spend 15 minutes meditating on a single word.",
    "Learn a magic trick and perform it for a friend.",
    "Create a piece of abstract art using only three colors.",
    "Write a letter to your future self.",
    "Go for a walk in nature and take photos of interesting textures.",
    "Listen to an album you've never heard before and write a review.",
    "Build a small project with a Raspberry Pi or Arduino.",
    "Learn a new programming language or framework.",
    "What if gravity worked sideways?",
    "Design a user interface for a time-traveling toaster.",
    "Imagine a world where plants could talk. What would they say?",
    "If you could have any superpower for a day, what would it be and how would you use it?",
    "Create a poem using only words found on street signs.",
    "Write a song about a cloud.",
]

def generate_inspiration():
    return random.choice(inspirations)

if st.button("Generate Inspiration"):
    with st.spinner("Generating..."):
        time.sleep(1)  # Simulate loading time
        st.write(generate_inspiration())

st.sidebar.header("Customization")
if st.sidebar.checkbox("Add your own inspiration?"):
    custom_inspiration = st.sidebar.text_area("Enter your inspiration:")
    if st.sidebar.button("Add"):
        if custom_inspiration:
            inspirations.append(custom_inspiration)
            st.sidebar.success("Inspiration added!")
        else:
            st.sidebar.error("Please enter some text.")

st.sidebar.header("About")
st.sidebar.write("This app generates random inspirations to spark creativity. Add your own ideas or prompts to the list!")

st.markdown("""
<style>
.big-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)