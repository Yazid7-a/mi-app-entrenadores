# alembic/env.py

import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# 1) Añade la carpeta raíz al PYTHONPATH para importar "app"
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 2) Importa la configuración, Base y todos los modelos
from app.core.config import settings
from app.core.database import Base

import app.models.user
import app.models.invitation
# si añades más modelos en el futuro:
# import app.models.message
# import app.models.measurement
# import app.models.event
# import app.models.notification

# 3) Configuración de Alembic
config = context.config

# 4) Logging
ini_file = config.config_file_name
assert ini_file is not None
fileConfig(ini_file)  # type: ignore[arg-type]

# 5) URL de la base de datos desde .env
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# 6) Metadata para autogenerate
target_metadata = Base.metadata  # type: ignore[attr-defined]

# --- Modo offline ---
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


# --- Modo online ---
def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:  # type: ignore[call-overload]
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # detecta cambios de tipo de columna
        )

        with context.begin_transaction():
            context.run_migrations()


# 7) Ejecutar según modo
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
