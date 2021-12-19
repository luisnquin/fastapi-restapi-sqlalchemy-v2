from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    from db.constants import *
else:
    from .constants import *


engine = create_engine(f"{DIALECT}://{USER}:{PASSWORD}@{HOST}/{NAME}")
Session = sessionmaker(engine)
session = Session()