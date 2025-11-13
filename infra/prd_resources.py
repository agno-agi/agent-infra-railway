"""Production Railway infrastructure resources."""
import os
from agno.railway import RailwayAgentOS, RailwayPostgres, RailwayResources
from infra.settings import infra_settings

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

# PostgreSQL Database
prd_postgres = RailwayPostgres(
    name=f"{infra_settings.prd_env}-test-db",
    postgres_version="16",
    database_name="test_agent_db",
    postgres_user="test_agent",
)

# AgentOS Application
prd_agentos = RailwayAgentOS(
    name=f"{infra_settings.prd_env}-test-agentos",

    # Docker image
    image_name=f"{infra_settings.image_repo}/{infra_settings.image_name}",
    image_tag="latest",

    # Database reference - this will automatically set DATABASE_URL
    database=prd_postgres,

    # Port configuration
    open_port=True,
    port_number=8000,

    # Uvicorn configuration
    uvicorn_host="0.0.0.0",
    uvicorn_port=8000,
    uvicorn_reload=False,
    uvicorn_log_level="info",
    web_concurrency=2,

    # AgentOS configuration
    agentos_ui_url="https://os.agno.com",
    enable_cors=True,

    # Environment variables
    env_vars={
        "ENVIRONMENT": "production",
        "LOG_LEVEL": "info",

        # Agent features
        "ENABLE_AGENTIC_MEMORY": "true",
        "MEMORY_PROVIDER": "postgres",

        "ANTHROPIC_API_KEY": "jnhs",

        # Metrics and monitoring
        "ENABLE_METRICS": "true",
        "ENABLE_EVALS": "true",
    },
)

# Railway Resources Configuration
prd_railway_config = RailwayResources(
    env=infra_settings.prd_env,
    name=f"{infra_settings.infra_name}-{infra_settings.prd_env}",

    # Applications
    apps=[prd_agentos],

    # Standalone resources
    resources=[prd_postgres],
)
