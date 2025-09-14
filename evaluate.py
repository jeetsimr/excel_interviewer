

import subprocess
import json

def evaluate_answer(question, answer, model="phi3"):
    
    prompt = f"""
    Imagine you are an Excel interviewer.
    Question: {question}
    Candidate Answer: {answer}

    Your job:
    - Give a score from 0 to 5 (just an integer).
    - Provide one helpful feedback line.

    Respond ONLY in JSON format like this:
    {{
        "score": 4,
        "feedback": "Answer is mostly correct but missed some details."
    }}
    """

    # Run Ollama model (change 'phi3' to 'mistral' or 'llama3' if you prefer)
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt.encode("utf-8"),
        capture_output=True
    )

   
    response = result.stdout.decode("utf-8").strip()

    try:
        return json.loads(response)
    except:
        return {"score": 0, "feedback": "Evaluation failed or response not in JSON format."}
