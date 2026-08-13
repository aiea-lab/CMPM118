import os
import subprocess
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

kb = open("../task4/harrypotter_kb.pl").read()

question = input("Question: ")

prompt = f"""
Convert this question into a Prolog query using the knowledge base.

Knowledge base:
{kb}

Question:
{question}

Return only the Prolog query.
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0
)

query = response.choices[0].message.content.strip()

query = query.replace("```prolog", "")
query = query.replace("```", "")
query = query.strip()
query = query.rstrip(".")

print("Prolog query:", query)

variable = query.split(",")[-1].strip().rstrip(")")

code = f"""
consult('../task4/harrypotter_kb.pl'),
(
    ({query})
    ->
    write({variable}),
    nl
    ;
    writeln('false')
),
halt.
"""

result = subprocess.run(
    ["swipl", "-q", "-g", code],
    capture_output=True,
    text=True
)

print("Answer:", result.stdout.strip())

if result.stderr:
    print("Error:", result.stderr)
