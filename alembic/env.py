import os
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Import Base and DATABASE_URL from the main application
from app.database import Base, DATABASE_URL
from app import models  # !!!User -> Base
# noqa: F401  # імпорт потрібен, щоб моделі зареєструвались у Base.metadata


# Alembic Config object, provides access to alembic.ini values
config = context.config

# Configure Python logging based on the alembic.ini file
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata that Alembic will use to autogenerate migrations
target_metadata = Base.metadata

# Replace the placeholder URL in alembic.ini with the actual DATABASE_URL
if DATABASE_URL:
    config.set_main_option("sqlalchemy.url", DATABASE_URL)
else:
    raise ValueError("DATABASE_URL is not set in .env")


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
