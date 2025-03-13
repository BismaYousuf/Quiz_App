import streamlit as st  
import random 
import time  


st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌟 QUIZ APPLICATION 🌟</h1>", unsafe_allow_html=True)


questions = [
    {
        "question": "What is the capital of Pakistan?",  
        "options": ['Karachi', 'Lahore', 'Islamabad', 'Peshawar'],  
        "answer": 'Islamabad'  
    },
    {
        "question": "Who is the founder of Pakistan?",
        "options": ["Allama Iqbal", "Liaquat Ali Khan", "Muhammad Ali Jinnah", "Benazir Bhutto"],
        "answer": "Muhammad Ali Jinnah",
    },
    {
        "question": "Which is the national language of Pakistan?",
        "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"],
        "answer": "Urdu",
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Rupee", "Dollar", "Taka", "Riyal"],
        "answer": "Rupee",
    },
    {
        "question": "Which city is known as the City of Lights in Pakistan?",
        "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"],
        "answer": "Karachi",
    },
]


if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)


question = st.session_state.current_question  

st.subheader(f"🧐 {question['question']}")


selected_option = st.radio("Choose your answer:", question["options"])


if st.button("Submit Answer", help="Click to check your answer!"):
    if selected_option == question["answer"]:
        st.success("🎉 Correct! Well done!") 
        st.balloons()
    else:
        st.error(f"❌ Incorrect! The correct answer is **{question['answer']}**.")  

    time.sleep(2)  

   
    st.session_state.current_question = random.choice(questions)

   
    st.rerun()
