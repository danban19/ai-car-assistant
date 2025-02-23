"""
Main entry point for the application with memory-based chat history for a car retailing 
assistant.
"""
import os

from openai import AsyncAzureOpenAI
import chainlit as cl

from prompts import CAR_ASSISTANT_PROMPT

client = AsyncAzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

cl.instrument_openai()
settings = {
    "model": "gpt-4o-mini",
    "temperature": 0
}
conversation_memory = {}

@cl.on_message
async def main(message: cl.Message) -> None:
    """
    Handle incoming messages, maintaining chat history and responding as a car retailing assistant.
    The assistant engages the user to gather information about their car preferences 
    (e.g., budget, car type, fuel type, brand, and specific features) and suggests suitable cars.
    Args:
        message (cl.Message): The incoming message from the user.
    Returns:
        None: No return value.
    """
    session_id = message.author

    if session_id not in conversation_memory:
        conversation_memory[session_id] = [
            {
                "role": "system",
                "content": (
                    CAR_ASSISTANT_PROMPT
                )
            }
        ]

    conversation_memory[session_id].append({"role": "user", "content": message.content})
    response = await client.chat.completions.create(
        messages=conversation_memory[session_id],
        **settings
    )
    assistant_reply = response.choices[0].message.content
    conversation_memory[session_id].append({"role": "assistant", "content": assistant_reply})

    await cl.Message(content=assistant_reply).send()
