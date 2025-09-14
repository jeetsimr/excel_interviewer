Excel Interview Simulation Bot
Project Overview:
This project simulates an Excel skills interview using a Python-based bot. 
The bot asks a series of Excel-related questions, collects answers, evaluates them using the Mistral LLM, and generates a summary report with scores and feedback.

Features:
1. Terminal-based mock interview.
2. Randomized question sequence for each run.
3. Automatic evaluation using Mistral.
4. Summary of answers and scores saved in 'summary.txt'.
5. Optional Excel file support for demonstration.

Files Included:
- app.py           : Main script to run the interview simulation.
- questions.py     : List of Excel questions.
- summary.txt      : Automatically generated output summary (sample included).
- README.txt       : This instruction file.

Requirements:
- Python 3.x installed.
- Mistral LLM installed and configured for answer evaluation.
-Streamlit installed (pip install streamlit) for web interface. 

How to Run:
1. Open a terminal and navigate to the project folder:
   cd excel_interviewer
2. Run the main script:
   python app.py
3. Follow the prompts to answer each question.
4. After completing all questions:
   - Terminal will display your feedback and scores.
   - 'summary.txt' will be created/updated with detailed scores and feedback.

Notes:
- Each run will shuffle the order of questions randomly.
Make sure Streamlit is installed:
 -pip install streamlit

 Run the Streamlit app:

  -streamlit run appstreamlit.py

The app will open in your browser. Answer questions interactively.

Note: Streamlit Cloud cannot run the Mistral LLM directly due to environment restrictions.

For full functionality using Mistral, run the app locally where Ollama CLI is installed
Future Improvements:
- Store multiple interview sessions with timestamps in 'summary.txt'.
- Add a web interface using Streamlit or Gradio for a more interactive experience.
- Optionally integrate a database to track user performance over multiple sessions.

Author:
simranjeet kaur 
Date:
14-9-2025

