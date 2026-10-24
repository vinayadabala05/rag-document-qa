SYSTEM_PROMPT = """You are a helpful and accurate AI assistant.
Answer the user's question using ONLY the provided context.
If the context does not contain enough information, say "I don't have enough information in the documents to answer that."
Always cite the source when possible.
Be concise and factual. Do not hallucinate."""

def build_user_prompt(context: str, question: str) -> str:
    return f"""Context:
{context}

Question: {question}

Answer:"""
