import streamlit as st
from modules.story_generator import generate_stories
from modules.model_loader import load_model

st.title("🧙 AI Dungeon Story Generator")

prompt = st.text_area("Enter your story prompt:")
genre = st.selectbox("Choose a genre", ["Fantasy", "Mystery", "Sci-Fi", "Adventure"])

if st.button("Generate Story"):
    model, tokenizer = load_model("gpt2")
    stories = generate_stories(model, tokenizer, prompt, genre)
    for idx, story in enumerate(stories):
        st.markdown(f"### Story Option {idx+1}")
        st.write(story)
    full_story = "\n\n".join(stories)
    st.download_button("Download Full Story", data=full_story, file_name="story.txt")
