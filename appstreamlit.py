import streamlit as st
import random
from questions import questions
from evaluate import evaluate_answer

st.title("📊 Excel Interview Simulation Bot")
st.write("Welcome! This is your Excel skills interview simulation. Answer the questions below briefly.")

if "results" not in st.session_state:
    st.session_state.results = []
if "asked_questions" not in st.session_state:
    shuffled = questions.copy()
    random.shuffle(shuffled)
    st.session_state.asked_questions = shuffled
if "current_index" not in st.session_state:
    st.session_state.current_index = 0

# Show current question
if st.session_state.current_index < len(st.session_state.asked_questions):
    q = st.session_state.asked_questions[st.session_state.current_index]
    st.subheader(f"Q{st.session_state.current_index + 1}: {q}")
    ans = st.text_area("Your Answer:", key=f"answer_{st.session_state.current_index}")

    if st.button("Submit Answer"):
        if ans.strip():
            feedback = evaluate_answer(q, ans)
            st.session_state.results.append(feedback)
            st.success(f"Feedback: {feedback['feedback']} | Score: {feedback['score']}/5")
            st.session_state.current_index += 1
        else:
            st.warning("Please enter an answer before submitting.")

else:
    st.subheader("✅ Interview Completed")
    avg_score = sum(r["score"] for r in st.session_state.results) / len(st.session_state.results)
    
    st.write("### Interview Summary")
    for i, r in enumerate(st.session_state.results, start=1):
        st.write(f"Q{i}: Score {r['score']} | {r['feedback']}")
    
    st.write(f"**Final Average Score: {avg_score:.2f}/5**")
    st.write("Thanks for participating in the mock interview!")
