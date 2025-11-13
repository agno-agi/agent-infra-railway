"""A simple assistant agent for Railway deployment."""

from agno.agent import Agent
from agno.models.anthropic import Claude

# Create agent
assistant_agent = Agent(
    name="Assistant",
    id="assistant-agent",
    model=Claude(id="claude-3-5-sonnet-20241022"),
    description="A helpful AI assistant deployed on Railway",
    instructions=[
        "You are a helpful AI assistant.",
        "Be concise and clear in your responses.",
        "You're deployed on Railway with PostgreSQL backing.",
    ],
    markdown=True,
    debug_mode=True,
)
