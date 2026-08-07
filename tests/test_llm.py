from src.llm import generate_response


prompt = """
You are an AI technical documentation assistant.

Explain in simple terms:
What is FastAPI?
"""

answer = generate_response(prompt)

print("\nAI Response:\n")
print(answer)