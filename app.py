import streamlit as st
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

# Streamlit page configuration
st.set_page_config(layout="wide")

# Title and description for the app
st.title("🟥 LLM End-to-End Project 👇")
st.title("🟥 1. AI Blog Companion")
st.subheader("👉 This application was built by Zia Ul Islam Mughal.")

# Sidebar for input details
with st.sidebar:
    st.title("👉 Input your blog details.")
    st.subheader("👉 Enter the details of the blog you want to generate.")
    
    # Input field for API key
    user_api_key = st.text_input("🔑 Enter your Google API Key", type="password")
    
    blog_title = st.text_input("👉 Blog Title")
    blog_keywords = st.text_area("👉 Enter keywords (comma separated)")
    num_words = st.slider("👉 Number of words", min_value=250, max_value=2000, step=100)

    submit_button = st.button("Generate Blog 👍")

# Ensure the API key is entered
if submit_button:
    if not user_api_key:
        st.error("Please enter a valid Google API key.")
    else:
        # Configure the API using the user's inputted key
        genai.configure(api_key=user_api_key)
        
        # Define the model generation configuration
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
        
        # Safety settings to avoid harmful content
        safety_settings = {
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        }

        # Initialize the generative model
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            safety_settings=safety_settings
        )

        # Generate prompt based on user inputs
        prompt_part = f"""
        Generate a comprehensive, engaging blog post relevant to the given title "{blog_title}"
        and keywords "{blog_keywords}". Make sure these keywords are incorporated in the blog post. 
        The blog should be approximately {num_words} words in length, suitable for an online audience. 
        Ensure the content is original, informative, and maintains a consistent tone throughout.
        """

        # Start chat session and generate the blog content
        chat_session = model.start_chat(history=[{"role": "user", "parts": [prompt_part]}])

        # Send the prompt to the chat model
        response = chat_session.send_message(prompt_part)

        # Display the generated blog content
        st.write("Your Blog Post 👇:")
        st.write("-----------------------------------------------------------------------------------------------------------")
        st.write(response.text)
