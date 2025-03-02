# Python & Third Party Imports
from threading import Lock

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

Base = declarative_base()


class DatabaseService:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        """Singleton implementation."""
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(DatabaseService, cls).__new__(cls)
        return cls._instance

    def __init__(
        self,
        database_name,
        user,
        password,
        host,
        port,
        echo,
        environment,
        test_database_name,
    ):
        if not hasattr(self, "_initialized"):
            self._initialized = True

            self.database_url = f"postgresql://{user}:{password}@{host}:{port}/{database_name if environment != 'test' else test_database_name}"

            self.engine = create_engine(
                self.database_url,
                echo=echo,
                pool_pre_ping=True,
            )

            print(f"DATABASE : {self.database_url}")

            self.session_factory = sessionmaker(bind=self.engine)
            self.Session = scoped_session(self.session_factory)

    def get_session(self):
        """Get a new session."""
        try:
            return self.Session()
        except SQLAlchemyError as e:
            print(f"Error while getting session: {e}")
            return None

    def close_connection(self):
        """Close the database connection."""
        self.Session.remove()
        self.engine.dispose()


db_service = DatabaseService(
    database_name="boilerplate_db",
    user="postgres",
    password="2589",
    host="localhost",
    port="5432",
    environment="DEVELOPMENT",
    echo=False,
    test_database_name="boilerplate_test_db",
)
