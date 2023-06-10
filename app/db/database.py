from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..config.settings import POSTGRESQL_DSN

engine = create_engine(POSTGRESQL_DSN)

service_session = sessionmaker(
    bind=create_engine(
        POSTGRESQL_DSN,
        pool_pre_ping=True,
        echo=False,
        connect_args={'connect_timeout': 60}
    ),
    autocommit=False,
    autoflush=False,
    future=True
)
