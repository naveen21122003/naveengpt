import streamlit as st
import google.generativeai as genai
genai.configure(api_key=st.secrets["api"])
def ai(txt):
    
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("வணக்கம் மக்களே என்னிடம் அனைத்து விதமான கேள்விகளுக்கும் பதில் கிடைக்கும்.: "+txt)
    return response.text


st.title("NAVEEN GPT")

if "messages" not in st.session_state:
    st.session_state.messages = []  # Use plural for clarity

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["message"])

message = st.chat_input("Your message")  # Singular for user input

if message:
    with st.chat_message("user"):
        st.write(message)
        st.session_state.messages.append({"role": "user", "message": message})
    if message.lower() == "hi":  # Make case-insensitive
        with st.chat_message("bot"):
            st.write("Hello! I am a Goolge Assistant.created by NaveenKumar")
            st.session_state.messages.append({"role": "bot", "message": "Hello"})
    elif message.lower() == "good morning":
        with st.chat_message("bot"):
            st.write("Good morning! Have a nice day")
            st.session_state.messages.append({"role": "bot", "message": "Good morning! Have a nice day"})
    elif message.lower() == "hello":
        with st.chat_message("bot"):
            st.write("Hello!")
            st.session_state.messages.append({"role": "bot", "message": "Good morning! Have a nice day"})
    else:
        with st.chat_message("bot"):
            data = ai(message)
            st.write(data)
            st.session_state.messages.append({"role": "bot", "message": data})




    
