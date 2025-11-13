"""Infrastructure settings for test Railway agent."""

from pathlib import Path
from agno.infra.settings import InfraSettings

# Get the project root directory
infra_root = Path(__file__).parent.parent.resolve()

# Infrastructure settings
infra_settings = InfraSettings(
    # Project identification
    infra_name="test-railway-agent",
    infra_root=infra_root,

    # Environment configuration
    dev_env="dev",
    prd_env="prd",
    default_env="dev",
    default_infra="railway",

    # Docker image configuration
    image_repo="uzairali10",
    image_name="test-railway-agent",

    # Railway will use environment variables:
    # - RAILWAY_API_TOKEN
    # - RAILWAY_WORKSPACE_ID
)
