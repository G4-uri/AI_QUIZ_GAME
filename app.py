import random
import time
import streamlit as st
from questions import QUESTIONS

st.set_page_config(
    page_title="AI Quiz Game - Units I & II",
    page_icon="🤖",
    layout="centered"
)

TOTAL_QUESTIONS = len(QUESTIONS)
QUIZ_TIME_SECONDS = 30 * 60

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

    # All 50 questions are used once, in random order.
    st.session_state.questions = QUESTIONS.copy()
    random.shuffle(st.session_state.questions)

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

    st.session_state.history.append(
        {
            "question": q["question"],
            "selected": st.session_state.selected,
            "selected_text": q["options"][st.session_state.selected],
            "correct_answer": q["answer"],
            "correct_text": q["options"][q["answer"]],
            "is_correct": correct,
            "explanation": q["explanation"],
        }
    )

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
    "A 50-question interactive quiz on AI foundations, agents, "
    "environments, search techniques, CSP, and means-end analysis."
)

if not st.session_state.started:

    if st.session_state.current >= TOTAL_QUESTIONS and st.session_state.history:
        score = st.session_state.score
        percentage = round((score / TOTAL_QUESTIONS) * 100, 2)

        st.success("🎉 Quiz completed successfully!")

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
            st.success("Excellent performance! You have a strong understanding of AI concepts.")
        elif percentage >= 50:
            st.info("Good attempt. Review the incorrect answers to improve further.")
        else:
            st.warning("Please revise Units I and II, then attempt the quiz again.")

        with st.expander("📋 Review all answers"):
            for i, item in enumerate(st.session_state.history, start=1):
                if item["is_correct"]:
                    status = "✅ Correct"
                else:
                    status = "❌ Incorrect"

                st.markdown(f"### Question {i}")
                st.markdown(f"**{item['question']}**")
                st.markdown(f"Your answer: **{item['selected_text']}**")
                st.markdown(f"Correct answer: **{item['correct_text']}**")
                st.markdown(f"Result: {status}")
                st.info(f"Explanation: {item['explanation']}")
                st.divider()

        if st.button("🔄 Start New Quiz Attempt", use_container_width=True):
            st.session_state.current = 0
            st.session_state.history = []
            start_quiz()
            st.rerun()

    else:
        st.markdown("### Game Rules")
        st.markdown(
            f"""
- The quiz contains **{TOTAL_QUESTIONS} unique questions** from Units I and II.
- All questions are displayed once, but the order is randomized in every attempt.
- Total time allowed: **30 minutes**.
- Each correct answer carries **1 mark**.
- Use the **Hint** button to view a concept clue.
- Use **50:50** to remove two incorrect options.
- Immediate feedback is provided after every answer.
- The progress bar indicates quiz completion.
- Your final score, percentage, result, and detailed answer review appear after Question 50.
            """
        )

        if st.button("🚀 Start 50-Question Quiz", use_container_width=True):
            start_quiz()
            st.rerun()

else:
    elapsed = time.time() - st.session_state.start_time
    remaining = max(0, int(QUIZ_TIME_SECONDS - elapsed))

    minutes = remaining // 60
    seconds = remaining % 60

    if remaining == 0:
        st.error("⏰ Time is over. Your quiz has been submitted.")
        st.session_state.started = False
        st.session_state.current = TOTAL_QUESTIONS
        st.rerun()

    q = st.session_state.questions[st.session_state.current]
    q_number = st.session_state.current + 1

    st.info(f"⏳ Time Remaining: **{minutes:02d}:{seconds:02d}**")

    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"### Question {q_number} of {TOTAL_QUESTIONS}")
    with col2:
        st.metric("Score", f"{st.session_state.score}/{q_number - 1}")

    st.progress(q_number / TOTAL_QUESTIONS)

    st.caption(
        f"Topic: {q['topic']}  |  Difficulty: {q['difficulty']}  |  Question Type: {q['type']}"
    )

    st.markdown(f"## {q['question']}")

    options = q["options"]

    visible_options = [
        i for i in range(len(options))
        if i not in st.session_state.hidden_options
    ]

    selected = st.radio(
        "Choose one answer:",
        options=visible_options,
        format_func=lambda index: options[index],
        index=None,
        key=f"question_{q['id']}",
        disabled=st.session_state.submitted
    )

    if not st.session_state.submitted:
        st.session_state.selected = selected

    button_col1, button_col2, button_col3 = st.columns(3)

    with button_col1:
        if st.button(
            "💡 Hint",
            disabled=st.session_state.hint_used or st.session_state.submitted,
            use_container_width=True
        ):
            st.session_state.hint_used = True
            st.info(f"Hint: {q['explanation']}")

    with button_col2:
        if st.button(
            "50:50",
            disabled=st.session_state.fifty_fifty_used or st.session_state.submitted,
            use_container_width=True
        ):
            correct_option = q["answer"]

            incorrect_options = [
                i for i in range(len(options))
                if i != correct_option
            ]

            random.shuffle(incorrect_options)

            # Hide up to two wrong answers.
            st.session_state.hidden_options = incorrect_options[:2]
            st.session_state.fifty_fifty_used = True
            st.rerun()

    with button_col3:
        if st.button(
            "Submit Answer",
            disabled=(
                st.session_state.selected is None
                or st.session_state.submitted
            ),
            use_container_width=True
        ):
            check_answer()
            st.rerun()

    if st.session_state.submitted:
        correct_index = q["answer"]

        if st.session_state.selected == correct_index:
            st.success("✅ Correct answer!")
        else:
            st.error("❌ Incorrect answer.")
            st.markdown(f"**Correct answer:** {options[correct_index]}")

        st.info(f"**Explanation:** {q['explanation']}")

        button_text = (
            "🏁 Finish Quiz"
            if q_number == TOTAL_QUESTIONS
            else "Next Question ➡️"
        )

        if st.button(button_text, use_container_width=True):
            next_question()
            st.rerun()