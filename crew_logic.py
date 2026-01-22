import os
from crewai import Agent, Task, Crew, LLM

llm = LLM(
    model="gemini/gemini-2.5-flash-lite",
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.0
)

os.environ["OPENAI_API_KEY"] = "NA"

assignment_analyzer = Agent(
    role="Assignment Analyzer",
    goal="Evaluate assignment quality and originality",
    backstory="An academic assistant who evaluates assignments like a teacher.",
    llm=llm,
    verbose=True
)

teacher_evaluator = Agent(
    role="Academic Evaluator",
    goal="Give teacher-style feedback and improvement guidance",
    backstory="A senior teacher focused on clarity, originality, and presentation.",
    llm=llm,
    verbose=True
)

def evaluate_assignment(assignment_text: str):

    analyze_task = Task(
        description=f"""
        Analyze the following student assignment:

        {assignment_text}

        Determine:
        - Overall quality (Good / Average / Poor)
        - Clarity and structure
        - Originality (Human-written or AI-like)
        """,
        expected_output="""
        Assignment quality rating with reasoning.
        """,
        agent=assignment_analyzer
    )

    feedback_task = Task(
        description="""
        Provide teacher-style feedback including:
        - What is good
        - What needs improvement
        - How to improve to impress the teacher
        - If AI-like, rewrite in a more human tone
        """,
        expected_output="Detailed academic feedback and improved version if needed.",
        agent=teacher_evaluator
    )

    crew = Crew(
        agents=[assignment_analyzer, teacher_evaluator],
        tasks=[analyze_task, feedback_task],
        planning=False,
        verbose=False
    )

    return crew.kickoff()
