import requests

def evaluate_answer(question, answer):
    prompt = f"""
    Question: {question}
    Answer: {answer}
    Score 0-5 + feedback
    """
    response = requests.post(
        "https://api.ollama.com/run/mistral",
        json={"prompt": prompt, "model": "mistral"},
        headers={"Authorization": "Bearer YOUR_API_KEY"}
    )
    data = response.json()
    return {"score": data["score"], "feedback": data["feedback"]}
