"""AgentOS application entry point for Railway deployment."""

from agno.os import AgentOS
from infra.agents import assistant_agent

# Create AgentOS instance with our assistant agent
agent_os = AgentOS(
    agents=[assistant_agent],
    # Add teams and workflows here if needed
)

# Get FastAPI app
app = agent_os.get_app()

if __name__ == "__main__":
    # For local development
    agent_os.serve(app="app:app", reload=True)
