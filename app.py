import streamlit as st

st.set_page_config(page_title="AI Content Generator")

st.title(" AI Content Generator")

# User Inputs
topic = st.text_input("Enter Topic")

tone = st.selectbox(
    "Select Tone",
    ["Professional", "Friendly", "Creative", "Motivational"]
)

content_type = st.selectbox(
    "Content Type",
    ["Blog Post", "Social Media Caption"]
)

# Content Generation Function
def generate_content(topic, tone, content_type):

    if content_type == "Blog Post":
        content = f"""
# {topic}

This is a {tone.lower()} blog post about {topic}.

{topic} is an important subject that impacts many people. Understanding its benefits and applications can help individuals make informed decisions.

In conclusion, {topic} continues to grow in importance and offers many opportunities for learning and development.
"""
    else:
        content = f"""
✨ {topic} ✨

Discover the power of {topic} today!

#Motivation #Learning #Success
"""

    return content

# Generate Button
if st.button("Generate Content"):

    if topic == "":
        st.error("Please enter a topic")
    else:
        result = generate_content(topic, tone, content_type)

        st.subheader("Generated Content")
        st.write(result)

        # Word Count
        word_count = len(result.split())

        # Character Count
        char_count = len(result)

        st.info(f"Word Count: {word_count}")
        st.info(f"Character Count: {char_count}")

        # Copy Option
        st.text_area("Copy Content", result, height=250)

# Regenerate Button
if st.button("Regenerate"):
    st.success("Generate Content button again.")
