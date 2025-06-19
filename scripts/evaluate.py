# scripts/evaluate.py

import os
import csv
import re
import time
import openai
from pathlib import Path
from tqdm import tqdm

# ─── 1) Configure OpenAI API key & model ───────────────────────────────
openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "gpt-4"

# ─── 2) Your evaluation prompt ────────────────────────────────────────
EVALUATION_PROMPT = """###Task Description:
An instruction (might include an Input inside it), a response to evaluate, a reference answer that gets a score of 5, and a score rubric representing a evaluation criteria are given.
Write a detailed feedback that assess the quality of the response strictly based on the given score rubric, not evaluating in general.
After writing a feedback, write a score that is an integer between 1 and 5. You should refer to the score rubric.
The output format should look as follows: "Feedback: {{write a feedback for criteria}} [RESULT] {{an integer number between 1 and 5}}"
Please do not generate any other opening, closing, and explanations. Be sure to include [RESULT] in your output.

###The instruction to evaluate:
{instruction}

###Response to evaluate:
{response}

###Reference Answer (Score 5):
{reference_answer}

###Score Rubrics:
[Is the response correct, accurate, and factual based on the reference answer?]
Score 1: The response is completely incorrect, inaccurate, and/or not factual.
Score 2: The response is mostly incorrect, inaccurate, and/or not factual.
Score 3: The response is somewhat correct, accurate, and/or factual.
Score 4: The response is mostly correct, accurate, and factual.
Score 5: The response is completely correct, accurate, and factual.

###Feedback:"""

# ─── 3) Parser for the model’s reply ───────────────────────────────────
def parse_feedback(raw: str) -> tuple[str, int]:
    """
    Extracts the Feedback text and the integer score from the model's reply.
    Expects format: "Feedback: ... [RESULT] X"
    """
    m = re.search(r"Feedback:(.*)\[RESULT\]\s*(\d+)", raw, re.S)
    if not m:
        # fallback: return the raw reply and a sentinel score
        return raw.strip(), -1
    feedback = m.group(1).strip()
    score = int(m.group(2))
    return feedback, score

# ─── 4) The main evaluation loop ──────────────────────────────────────
def main(
    infile: Path = Path("data/eval_questions.csv"),
    outfile: Path = Path("data/eval_results_openai.csv"),
    delay: float = 0.5,   # seconds between calls to avoid rate limits
):
    if openai.api_key is None:
        raise RuntimeError("Please set OPENAI_API_KEY in your environment")

    # Prepare input/output
    with infile.open(newline="", encoding="utf-8") as f_in, \
         outfile.open("w", newline="", encoding="utf-8") as f_out:

        reader = csv.DictReader(f_in)
        fieldnames = reader.fieldnames + ["feedback", "score"]
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        writer.writeheader()

        for row in tqdm(reader, desc="Evaluating with OpenAI"):
            prompt = EVALUATION_PROMPT.format(
                instruction=row["instruction"],
                response=row["response"],
                reference_answer=row["reference_answer"],
            )

            # Call OpenAI ChatCompletion
            resp = openai.ChatCompletion.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
            )
            text = resp.choices[0].message.content

            feedback, score = parse_feedback(text)
            row.update({"feedback": feedback, "score": score})
            writer.writerow(row)

            # throttle to respect rate limits
            time.sleep(delay)

    print(f"✅ Evaluation complete — results in {outfile}")

if __name__ == "__main__":
    main()
