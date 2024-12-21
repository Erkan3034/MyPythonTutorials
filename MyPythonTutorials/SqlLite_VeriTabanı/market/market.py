import sqlite3

class Product():
    def __init__(self, name, id, price, amount):
        self.name = name
        self.id = id
        self.price = price
        self.amount = amount

    def __str__(self):
        return ("Product Name: {}\n"
                "Product Id: {}\n"
                "Product Price: {}\n"
                "Product Amount: {}\n".format(self.name, self.id, self.price, self.amount))


class Market:
    def __init__(self):
        self.connectdb()

    def connectdb(self):
        self.con = sqlite3.connect("market.db")
        self.cursor = self.con.cursor()
        query = "CREATE TABLE IF NOT EXISTS products(name TEXT , id INT, price DOUBLE , amount INT)"
        self.cursor.execute(query)
        self.con.commit()

    def disconnect(self):
        self.con.close()

    def list_products(self):
        query = "SELECT * FROM products"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def search_product(self, name):
        query = "SELECT * FROM products WHERE name = ?"
        self.cursor.execute(query, (name,))
        return self.cursor.fetchall()

    def add_product(self, product_to_add):
        query = "INSERT INTO products VALUES(?,?,?,?)"
        self.cursor.execute(query, (product_to_add.name, product_to_add.id, product_to_add.price, product_to_add.amount))
        self.con.commit()

    def delete_product(self, name):
        query = "DELETE FROM products WHERE name = ?"
        self.cursor.execute(query, (name,))
        self.con.commit()

    def increase_amount(self, name):
        query = "SELECT * FROM products WHERE name = ?"
        self.cursor.execute(query, (name,))
        product = self.cursor.fetchone()
        if product:
            amount = product[3] + 1
            update_query = "UPDATE products SET amount = ? WHERE name = ?"
            self.cursor.execute(update_query, (amount, name))
            self.con.commit()
            return True
        return False
