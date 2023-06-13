# connection.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Classe para conexão com o db
class Connection:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        

    # Retorna uma nova sessão com o db
    def get_session(self):
        return self.Session()