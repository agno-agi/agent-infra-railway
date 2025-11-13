"""A simple assistant agent for Railway deployment."""
from os import getenv
from agno.agent import Agent
from agno.db.postgres import PostgresDb
from agno.models.anthropic import Claude

def get_db_url() -> str:
    db_driver = getenv("DB_DRIVER", "postgresql+psycopg")
    db_user = getenv("DB_USER") or getenv("PGUSER")
    db_pass = getenv("DB_PASS") or getenv("PGPASSWORD")
    db_host = getenv("DB_HOST") or getenv("PGHOST")
    db_port = getenv("DB_PORT") or getenv("PGPORT")
    db_database = getenv("DB_DATABASE") or getenv("PGDATABASE")
    return "{}://{}{}@{}:{}/{}".format(
        db_driver,
        db_user,
        f":{db_pass}" if db_pass else "",
        db_host,
        db_port,
        db_database,
    )

db_url=get_db_url()

# Create agent
assistant_agent = Agent(
    name="Assistant",
    id="assistant-agent",
    db=PostgresDb(db_url=db_url, session_table="sage_sessions"),
    model=Claude(id="claude-sonnet-4-5-20250929"),
    description="A helpful AI assistant deployed on Railway",
    instructions=[
        "You are a helpful AI assistant.",
        "Be concise and clear in your responses.",
        "You're deployed on Railway with PostgreSQL backing.",
    ],
    markdown=True,
    debug_mode=True,
)
