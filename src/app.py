"""Main entry point for the application."""
import chainlit as cl


@cl.on_message
async def main(message: cl.Message) -> None:
    """Endpoint for handling messages.
    Args:
        message (cl.Message): The message
    Returns:
        None
    """

    await cl.Message(
        content=f"Received: {message.content}",
    ).send()
