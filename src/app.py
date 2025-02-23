"""Main entry point for the application."""
import os

from openai import AsyncAzureOpenAI
import chainlit as cl


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

@cl.on_message
async def main(message: cl.Message) -> None:
    """Endpoint for handling messages.
    Args:
        message (cl.Message): The message
    Returns:
        None
    """
    response = await client.chat.completions.create(
        messages=[
            {
                "content": "You are a helpful bot.",
                "role": "system"
            },
            {
                "content": message.content,
                "role": "user"
            }
        ],
        **settings
    )
    await cl.Message(content=response.choices[0].message.content).send()
