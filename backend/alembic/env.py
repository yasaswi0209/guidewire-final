from logging.config import fileConfig
from sqlalchemy import create_engine
from alembic import context
import os
from dotenv import load_dotenv

from app.db.base import Base

# Load environment variables
load_dotenv()

# Alembic Config object
config = context.config

# Logging setup
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata
target_metadata = Base.metadata


# -----------------------------
# OFFLINE MODE
# -----------------------------
def run_migrations_offline() -> None:
    """Run migrations in offline mode."""
    
    DATABASE_URL = os.getenv("DATABASE_URL")

    if not DATABASE_URL:
        raise ValueError("DATABASE_URL is not set")

    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


# -----------------------------
# ONLINE MODE
# -----------------------------
def run_migrations_online() -> None:
    """Run migrations in online mode."""

    DATABASE_URL = os.getenv("DATABASE_URL")

    if not DATABASE_URL:
        raise ValueError("DATABASE_URL is not set")

    connectable = create_engine(DATABASE_URL)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


# -----------------------------
# RUN
# -----------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()