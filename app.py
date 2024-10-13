import streamlit as st 
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from APIKEY import google_api_key

 
genai.configure(api_key=google_api_key)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}    
safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    }

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
   safety_settings = safety_settings
)





st.set_page_config(layout="wide")

# Title of app
st.title("🟥 LLM End to End Project . 👇")
st.title("🟥 1. Ai Blog Companion")
st.subheader("👉This application build by Zia Ul Islam Mughal.")




with st.sidebar:
    st.title("👉Input your blog details.")
    st.subheader("👉Enter detail of blog you want to generate.")
    
    
    blog_title = st.text_input("👉Blog Title")
    blog_keywords = st.text_area("👉Enter keywords (comma sperated)")
    num_words = st.slider("👉Numer of words",min_value=250,max_value=2000,step=100)


    prompt_part = [f"""Generate a comprehensive, engaging blog post relevant to the given title{blog_title } 
    and keywords {blog_keywords } .Make sure these keywords incoparte in blog post .  The blog 
    should be approximately {num_words } words in length, suitable for an online audience. Ensure the content 
    is original, informative, and maintains a consistent tone throughout."""]
    
    
    chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [f"""Generate a comprehensive, engaging blog post relevant to the given title{blog_title } 
    and keywords {blog_keywords } .Make sure these keywords incoparte in blog post .  The blog 
    should be approximately {num_words } words in length, suitable for an online audience. Ensure the content 
    is original, informative, and maintains a consistent tone throughout."""],
    },
    {
      "role": "model",
      "parts": [f"""Generate a comprehensive, engaging blog post relevant to the given title{blog_title } 
    and keywords {blog_keywords } .Make sure these keywords incoparte in blog post .  The blog 
    should be approximately {num_words } words in length, suitable for an online audience. Ensure the content 
    is original, informative, and maintains a consistent tone throughout."""],
    },
  ]
)

    submit_button = st.button("Generate Blog👍")
    
if submit_button : 
    
    response = chat_session.send_message("prompt_part")
   
    



    st.write("Your Blog is Post 👇 : \n")
    st.write("-----------------------------------------------------------------------------------------------------------")

    st.write(response.text)