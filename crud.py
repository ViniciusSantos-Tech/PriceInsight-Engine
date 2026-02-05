from database import get_session, Tabel
from sqlalchemy.exc import SQLAlchemyError
class Crud():
    def __init__(self):
        self.session = get_session()
    def add_history(self, Product:str, Price: str) -> tuple[bool, str]:
        try:
            new_register = Tabel(Product=Product, Price=Price)
            self.session.add(new_register)
            self.session.commit()
            return True, 'Added to database.'
        except SQLAlchemyError as e:
            self.session.rollback()
            return False, f"Could not insert data: {e}"
        finally:
            self.session.close()


 
