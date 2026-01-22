import streamlit as st
from crew_logic import evaluate_assignment
import datetime

# ---------- Page Config ----------
st.set_page_config(
    page_title="AI Assignment Evaluation Agent",
    page_icon="🎓",
    layout="wide"
)

# ---------- Sidebar Styling ----------
st.markdown("""
<style>
section[data-testid="stSidebar"] {
    background-color: #0b1c2d;
}
section[data-testid="stSidebar"] * {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------- Button Styling ----------
st.markdown("""
<style>
div.stButton > button {
    background-color: #4da3ff;   /* light blue */
    color: white;                /* white text */
    border-radius: 8px;
    height: 3em;
    font-size: 16px;
    font-weight: 600;
}
div.stButton > button:hover {
    background-color: #1e81e8;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* Sidebar logo – REAL outline using drop-shadow */
section[data-testid="stSidebar"] img {
    background-color: transparent;
    padding: 0;

    /* Remove box effects */
    border: none;
    border-radius: 0;

    /* REAL outline + glow following logo shape */
    filter:
        drop-shadow(0 0 2px white)
        drop-shadow(0 0 6px rgba(255,255,255,0.8))
        drop-shadow(0 0 12px rgba(255,255,255,0.5));
}
</style>
""", unsafe_allow_html=True)


# ---------- Sidebar ----------
st.sidebar.image("logo.png", width=180)
st.sidebar.title("🎓 Assignment Evaluator")
st.sidebar.write("CrewAI based academic assistant")

if "history" not in st.session_state:
    st.session_state.history = []


# ---------- Main UI ----------
col1, col2 = st.columns([1, 6])

with col1:
    st.image("logo.png", width=150)

with col2:
    st.markdown(
        "<h1 style='margin-bottom:0;'>AI Assignment Evaluation Agent</h1>",
        unsafe_allow_html=True
    )
    st.caption("Professional academic evaluation using CrewAI multi-agent system")


st.divider()

assignment_text = st.text_area(
    "📄 Paste your assignment here",
    height=280,
    placeholder="Paste theory or short programming assignment here..."
)

if st.button("🔍 Evaluate Assignment", use_container_width=True):
    if assignment_text.strip() == "":
        st.warning("Please paste an assignment first.")
    else:
        with st.spinner("Evaluating assignment like a teacher..."):
            result = evaluate_assignment(assignment_text)

        from uuid import uuid4
        evaluation_id = str(uuid4())[:8]

        # ---------- Output ----------
        st.success("✅ Evaluation Completed")

        st.subheader("🧠 Teacher-Style Evaluation")

        st.markdown(
          f"""
           <div style="
           background-color:#f5f7fa;
           padding:20px;
           border-radius:10px;
           border-left:6px solid #4da3ff;
           color:#000000;
           font-size:15px;
           line-height:1.6;
           ">
           {result}
           </div>
           """,
           unsafe_allow_html=True
                    )

        st.info(
            "💡 Tip: Use the improvement suggestions above to refine your assignment "
            "so it appears more human-written and teacher-impressive."
        )
