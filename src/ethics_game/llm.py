from ollama import chat
from ollama import ChatResponse

from typing import List

def call(
    system_prompt: str,
    history: List[str],
) -> str:
    
    messages: List[str] = [{"role": "system", "content": system_prompt}] + history

    response: ChatResponse = chat(
        model='llama3.2',
        messages=messages,
    )

    return response.message.content