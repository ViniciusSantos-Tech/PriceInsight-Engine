from database import get_session, Tabel
class Crud():
    def __init__(self):
        self.session = get_session()
    def add_history(self, Product, Price):
        try:
            new_register = Tabel(Product=Product, Price=Price)
            self.session.add(new_register)
            self.session.commit()
            return {"Status": 200}
        except Exception as e:
            self.session.rollback()
            return {"Status": "Error", "Type": e}
        finally:
            self.session.close()
    def find_last_price(self):
        prices = self.session.query(Tabel).all()
        return prices

 