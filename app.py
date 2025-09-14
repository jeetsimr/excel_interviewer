import random
from questions import questions
from evaluate import evaluate_answer

def start_mock_interview():
    print("Welcome! This is your Excel skills interview simulation.")
    print("You will be asked a few questions. Please type your answers briefly.\n")

    # Make a copy of questions and shuffle it
    shuffled_questions = questions.copy()
    random.shuffle(shuffled_questions)

    results = []
    for i, q in enumerate(shuffled_questions, start=1):
        print(f"Q{i}: {q}")
        ans = input("Your Answer: ")

        feedback = evaluate_answer(q, ans)
        print(f"Feedback: {feedback['feedback']} | Score: {feedback['score']}/5\n")

        results.append(feedback)

    avg_score = sum(r["score"] for r in results) / len(results)

    # Print summary in terminal
    print("\n===== Interview Summary =====")
    for i, r in enumerate(results, start=1):
        print(f"Q{i}: Score {r['score']} | {r['feedback']}")
    print(f"\nFinal Average Score: {avg_score:.2f}/5")
    print("Thanks for participating in the mock interview!")

    # Save summary to summary.txt
    with open("summary.txt", "w") as f:
        f.write("===== Interview Summary =====\n")
        for i, r in enumerate(results, start=1):
            f.write(f"Q{i}: Score {r['score']} | {r['feedback']}\n")
        f.write(f"\nFinal Average Score: {avg_score:.2f}/5\n")
        f.write("Thanks for participating in the mock interview!\n")

if __name__ == "__main__":
    start_mock_interview()
