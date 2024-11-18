import os
import streamlit as st
import google.generativeai as genai
import PyPDF2
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Extract text from uploaded PDF
def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    extracted_text = ""
    for page in pdf_reader.pages:
        extracted_text += page.extract_text()
    return extracted_text

# Start the Streamlit App
st.title("Virtual HR - Mock Interview Simulator")

# Step 1: Resume Upload
uploaded_file = st.file_uploader("Upload your resume (PDF format)", type="pdf")
if uploaded_file:
    with st.spinner("Extracting text from your resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)
    st.success("Resume uploaded and processed successfully!")
else:
    resume_text = None

# Step 2: Job Role/Description
job_role = st.text_input("Enter the job role or description you're applying for:")
if job_role:
    st.success(f"Job role entered: {job_role}")

# Initialize session state for the interview
if "chat" not in st.session_state:
    st.session_state["chat"] = None
if "response" not in st.session_state:
    st.session_state["response"] = None
if "ongoing" not in st.session_state:
    st.session_state["ongoing"] = False

# Step 3: Start Mock Interview
if st.button("Start Mock Interview") and resume_text and job_role:
    with st.spinner("Starting the interview..."):
        st.session_state["chat"] = genai.GenerativeModel("gemini-1.5-flash").start_chat(
            history=[
                {"role": "user", "parts": f"My resume: {resume_text}"},
                {"role": "user", "parts": f"I'm applying for the role of {job_role}. Start a mock interview."},
            ]
        )
        response = st.session_state["chat"].send_message("Begin the interview.")
        st.session_state["response"] = response.text
        st.session_state["ongoing"] = True

# Interactive Q&A Loop
if st.session_state["ongoing"]:
    # Display the interviewer's question
    if st.session_state["response"]:
        st.write(f"**Interviewer:** {st.session_state['response']}")
    
    # User's response input
    user_input = st.text_input("Your response:", key=f"user_input_{len(st.session_state['chat'].history)}")
    
    if st.button("Submit Response", key=f"submit_{len(st.session_state['chat'].history)}"):
        with st.spinner("Generating the next question..."):
            response = st.session_state["chat"].send_message(user_input)
            st.session_state["response"] = response.text

        # Reset state to emulate rerun
            st.session_state["user_input"] = ""
            st.session_state["ongoing"] = True
            st.query_params.clear()  # Clear query params to trigger a rerun



# Footer
st.markdown("---")
st.markdown("Powered by Google Gemini API and Streamlit")

