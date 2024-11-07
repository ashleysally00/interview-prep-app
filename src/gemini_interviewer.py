# src/gemini_interviewer.py

import google.generativeai as genai
import streamlit as st

# Define the Gemini AI model
model = genai.GenerativeModel('gemini-pro')

# Candidate details
DEFAULT_CONTEXT = {
    "age": 25,
    "gender": "female",
    "location": "Tunisia",
    "current_job_type": "graduate student",
    "new_job_type": "software engineer"
}

def start_interview():
    """Initialize the first question of the interview."""
    return "Tell me about yourself and why you are interested in this role."

def analyze_response_and_prompt_next_question(user_response, previous_prompt, context=DEFAULT_CONTEXT):
    """Analyze the user's response and generate the next question."""
    prompt = f"""
    **Interviewer:** {previous_prompt}

    **Candidate:** "{user_response}"

    You are a career coach role playing as interviewer with the user to improve their performance during interviews. 
    You are interviewing a {context['age']}-year-old {context['gender']} from {context['location']} 
    transitioning from {context['current_job_type']} to {context['new_job_type']}.

    As the interviewer:
    1. Provide brief, constructive feedback on the candidate's response
    2. Focus on confidence and communication skills
    3. If needed, suggest a more confident way to phrase their response
    4. Ask a natural follow-up question that explores their:
       - Professional experience
       - Problem-solving abilities
       - Teamwork and collaboration
       - Technical skills relevant to {context['new_job_type']}
    
    Keep your response concise and conversational. Format your response as:
    [Your feedback]
    
    Next question: [Your follow-up question]
    """

    try:
        # Generate response from Gemini
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        st.error(f"Error generating response: {str(e)}")
        return "I apologize, but I encountered an error. Could you please rephrase your response?"

def update_interview_context(age=None, gender=None, location=None, 
                           current_job=None, desired_job=None):
    """Update the interview context with new candidate details."""
    context = DEFAULT_CONTEXT.copy()
    if age: context['age'] = age
    if gender: context['gender'] = gender
    if location: context['location'] = location
    if current_job: context['current_job_type'] = current_job
    if desired_job: context['new_job_type'] = desired_job
    return context