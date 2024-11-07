import streamlit as st
import google.generativeai as genai
import os
from src.confidence_quiz import ConfidenceQuiz
from src.gemini_interviewer import analyze_response_and_prompt_next_question, start_interview
from src.utils import load_css, init_session_state, reset_session_state

# Page configuration
st.set_page_config(
    page_title="Interview Preparation Assistant",
    page_icon="👔",
    layout="wide"
)

# Initialize session state
init_session_state()
load_css()

# Main title
st.title("Interview Preparation Assistant")
st.markdown("---")

# Create two columns for the layout
col1, col2 = st.columns(2)

# Left Column - Confidence Quiz
with col1:
    st.header("Confidence Assessment")
    quiz = ConfidenceQuiz()

    if not st.session_state.quiz_started:
        st.markdown("""
        <div class="quiz-section">
            Take our confidence assessment to get personalized advice for your interview preparation.
        </div>
        """, unsafe_allow_html=True)
        if st.button("Start Quiz"):
            st.session_state.quiz_started = True
            st.rerun()  # Changed from experimental_rerun

    elif not st.session_state.quiz_complete:
        current_q = quiz.questions[st.session_state.current_question]
        
        st.markdown(f"""
        <div class="quiz-section">
            <h3>Question {current_q['id']} of 5</h3>
            <p>{current_q['question']}</p>
        </div>
        """, unsafe_allow_html=True)

        # Display options as radio buttons
        answer = st.radio(
            "Choose your answer:",
            list(current_q['options'].items()),
            format_func=lambda x: f"{x[0]}) {x[1]}"
        )

        if st.button("Next"):
            st.session_state.quiz_answers.append(answer[0])
            if st.session_state.current_question < len(quiz.questions) - 1:
                st.session_state.current_question += 1
                st.rerun()  # Changed from experimental_rerun
            else:
                st.session_state.quiz_complete = True
                st.rerun()  # Changed from experimental_rerun

    else:
        # Calculate and display results
        results = quiz.calculate_score(st.session_state.quiz_answers)
        
        st.markdown(f"""
        <div class="quiz-section">
            <h3>Your Results</h3>
            <p>Score: {results['score']} out of {results['max_score']}</p>
            <p>Confidence Level: {results['feedback']['level']}</p>
            <p>{results['feedback']['summary']}</p>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("View Detailed Feedback"):
            st.subheader("Your Strengths")
            for strength in results['feedback']['strengths']:
                st.markdown(f"- {strength}")
            
            st.subheader("Recommended Next Steps")
            for step in results['feedback']['next_steps']:
                st.markdown(f"- {step}")
            
            st.subheader("Interview Tips")
            for tip in results['feedback']['interview_tips']:
                st.markdown(f"- {tip}")

        if st.button("Retake Quiz"):
            reset_session_state()
            st.rerun()  # Changed from experimental_rerun

# Right Column - Interview Practice
with col2:
    st.header("Interview Practice")
    
    # Display current question
    st.markdown(
        f'<div class="interviewer-question">'
        f'<strong>Interviewer:</strong> {st.session_state.interview_prompt}'
        f'</div>',
        unsafe_allow_html=True
    )

    # User response input
    user_response = st.text_area("Your response:", height=150)

    # Submit and Reset buttons in two columns
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Submit Response"):
            if user_response.strip():
                try:
                    feedback = analyze_response_and_prompt_next_question(
                        user_response,
                        st.session_state.interview_prompt
                    )
                    st.session_state.interview_prompt = feedback
                    st.rerun()  # Changed from experimental_rerun
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
            else:
                st.warning("Please provide a response before submitting.")

    with col2:
        if st.button("Reset Interview"):
            st.session_state.interview_prompt = start_interview()
            st.rerun()  # Changed from experimental_rerun

if __name__ == "__main__":
    # Configure Gemini API
    if 'GOOGLE_API_KEY' in st.secrets:
        genai.configure(api_key=st.secrets['GOOGLE_API_KEY'])
    else:
        st.error("Missing Google API key in secrets!")