import random
import time
import streamlit as st
from questions import QUESTIONS

st.set_page_config(
    page_title="AI Quiz Game - Units I & II",
    page_icon="🤖",
    layout="centered"
)

TOTAL_QUESTIONS = 10
QUIZ_TIME_SECONDS = 10 * 60

if "started" not in st.session_state:
    st.session_state.started = False
if "questions" not in st.session_state:
    st.session_state.questions = []
if "current" not in st.session_state:
    st.session_state.current = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "selected" not in st.session_state:
    st.session_state.selected = None
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "hint_used" not in st.session_state:
    st.session_state.hint_used = False
if "fifty_fifty_used" not in st.session_state:
    st.session_state.fifty_fifty_used = False
if "hidden_options" not in st.session_state:
    st.session_state.hidden_options = []
if "history" not in st.session_state:
    st.session_state.history = []

def start_quiz():
    st.session_state.started = True
    st.session_state.questions = random.sample(
        QUESTIONS, TOTAL_QUESTIONS
    )
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.selected = None
    st.session_state.submitted = False
    st.session_state.start_time = time.time()
    st.session_state.hint_used = False
    st.session_state.fifty_fifty_used = False
    st.session_state.hidden_options = []
    st.session_state.history = []

def check_answer():
    q = st.session_state.questions[st.session_state.current]
    correct = st.session_state.selected == q["answer"]
    if correct:
        st.session_state.score += 1
    st.session_state.history.append({
        "question": q["question"],
        "selected": st.session_state.selected,
        "correct_answer": q["answer"],
        "is_correct": correct
    })
    st.session_state.submitted = True

def next_question():
    st.session_state.current += 1
    st.session_state.selected = None
    st.session_state.submitted = False
    st.session_state.hint_used = False
    st.session_state.fifty_fifty_used = False
    st.session_state.hidden_options = []

    if st.session_state.current >= TOTAL_QUESTIONS:
        st.session_state.started = False

st.title("🤖 Interactive AI Quiz Game")
st.subheader("Artificial Intelligence — Units I & II")
st.caption(
    "Covers AI foundations, agents, environments, search, heuristics, "
    "CSP, and means-end analysis."
)

if not st.session_state.started:
    if st.session_state.current >= TOTAL_QUESTIONS and st.session_state.history:
        score = st.session_state.score
        percentage = round((score / TOTAL_QUESTIONS) * 100, 2)

        st.success("Quiz completed!")

        col1, col2, col3 = st.columns(3)
        col1.metric("Score", f"{score}/{TOTAL_QUESTIONS}")
        col2.metric("Percentage", f"{percentage}%")
        col3.metric(
            "Result",
            "Pass ✅" if percentage >= 50 else "Try Again ❌"
        )

        st.progress(score / TOTAL_QUESTIONS)

        if percentage >= 80:
            st.balloons()
            st.info("Excellent! You have a strong understanding of AI concepts.")
        elif percentage >= 50:
            st.info("Good work! Revise the topics you missed.")
        else:
            st.warning("Please revise Units I and II and try again.")

        with st.expander("📋 Review your answers"):
            for i, item in enumerate(st.session_state.history, 1):
                status = "✅ Correct" if item["is_correct"] else "❌ Incorrect"
                st.markdown(
                    f"**Q{i}. {item['question']}**  \n"
                    f"Your answer: **{item['selected']}**  \n"
                    f"Correct answer: **{item['correct_answer']}**  \n"
                    f"{status}"
                )

    st.markdown("### Game Rules")
    st.markdown(
        f"""
- Each student receives **{TOTAL_QUESTIONS} randomly selected questions** from a bank of **50 questions**.
- Total time: **10 minutes**.
- Each correct answer gives **1 mark**.
- Use **Hint** for an explanation-based clue.
- Use **50:50** once per question to remove two incorrect options.
- Immediate feedback is shown after every answer.
- A progress bar and final score are displayed.
        """
    )

    if st.button("🚀 Start Quiz", use_container_width=True):
        start_quiz()
        st.rerun()

else:
    elapsed = time.time() - st.session_state.start_time
    remaining = max(0, int(QUIZ_TIME_SECONDS - elapsed))
    minutes = remaining // 60
    seconds = remaining % 60

    if remaining == 0:
        st.error("⏰ Time is over! Quiz submitted automatically.")
        st.session_state.started = False
        st.rerun()

    st.info(f"⏳ Time remaining: **{minutes:02d}:{seconds:02d}**")

    q = st.session_state.questions[st.session_state.current]
    q_number = st.session_state.current + 1

    st.markdown(f"### Question {q_number} of {TOTAL_QUESTIONS}")
    st.progress(q_number / TOTAL_QUESTIONS)
    st.caption(
        f"Topic: {q['topic']} | Difficulty: {q['difficulty']} | Type: {q['type']}"
    )
    st.markdown(f"**{q['question']}**")

    options = q["options"]
    display_options = []

    for index, option in enumerate(options):
        if index in st.session_state.hidden_options:
            continue
        display_options.append((index, option))

    selected = st.radio(
        "Choose your answer:",
        options=[index for index, _ in display_options],
        format_func=lambda index: options[index],
        index=None,
        key=f"question_{q['id']}"
    )
    st.session_state.selected = selected

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("💡 Hint", disabled=st.session_state.hint_used):
            st.session_state.hint_used = True
            st.info(q["explanation"])

    with col2:
        if st.button(
            "50:50",
            disabled=st.session_state.fifty_fifty_used or st.session_state.submitted
        ):
            correct = q["answer"]
            wrong_options = [
                i for i in range(len(options)) if i != correct
            ]
            random.shuffle(wrong_options)
            st.session_state.hidden_options = wrong_options[:2]
            st.session_state.fifty_fifty_used = True
            st.rerun()

    with col3:
        if st.button(
            "Submit Answer",
            disabled=st.session_state.selected is None or st.session_state.submitted,
            use_container_width=True
        ):
            check_answer()
            st.rerun()

    if st.session_state.submitted:
        correct_index = q["answer"]
        if st.session_state.selected == correct_index:
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect.")
            st.markdown(
                f"**Correct answer:** {options[correct_index]}"
            )

        st.info(f"**Explanation:** {q['explanation']}")

        if st.button("Next Question ➡️", use_container_width=True):
            next_question()
            st.rerun()