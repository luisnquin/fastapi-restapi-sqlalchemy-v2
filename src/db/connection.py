from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

try:
    from .constants import DIALECT, USER, PASSWORD, HOST, NAME
except ImportError:
    from constants import DIALECT, USER, PASSWORD, HOST, NAME


engine = create_engine(f"{DIALECT}://{USER}:{PASSWORD}@{HOST}/{NAME}")
Session = sessionmaker(engine)
session = Session()