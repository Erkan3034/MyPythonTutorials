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
                "Product Amount: {}\n".format(self.name,self.id,self.price,self.amount))


class Market:

    def __init__(self):
        self.connectdb()

    def connectdb(self):
        self.con = sqlite3.connect("market.db")
        self.cursor = self.con.cursor()

        query = "CREATE TABLE IF NOT EXISTS products(name TEXT , id INT  , price DOUBLE , amount INT)"

        self.cursor.execute(query)
        self.con.commit()


    def disconnect(self):

        self.con.close()

    def list_products(self):

        query = "SELECT * FROM products"
        self.cursor.execute(query)

        products = self.cursor.fetchall()

        if len(products)==0:
            print("There is no product.")

        else:
            for i in products:

                product = Product(i[0],i[1],i[2],i[3])
                print(product)
                print("")


    def search_product(self,searched_name):

        query = "SELECT * FROM products WHERE name = ?"

        self.cursor.execute(query,(searched_name,))

        products = self.cursor.fetchall()

        if len(products) == 0:
            print("There is no product you're looking for!")

        else:
            product = Product(products[0][0], products[0][1], products[0][2], products[0][3])
            print(product)



    def add_product(self,product_to_add):

        query = "INSERT INTO products VALUES(?,?,?,?)"
        self.cursor.execute(query,(product_to_add.name,product_to_add.id,product_to_add.price,product_to_add.amount))
        self.con.commit()


    def delete_product(self,product_to_del):
        query = "DELETE FROM products WHERE name = ?"
        self.cursor.execute(query,(product_to_del,))
        self.con.commit()

    def increase_amount(self,product_to_inc):
        query = "SELECT * FROM products WHERE name = ?"
        self.cursor.execute(query,(product_to_inc,))

        products = self.cursor.fetchall()

        if len(products) == 0:
            print("There is no product you're looking for!")

        else:
            amount = products[0][3]
            amount+=1

            query2 =" UPDATE products SET amount = ?  WHERE amount = ?"
            self.cursor.execute(query2,(amount,product_to_inc,))
            self.con.commit()
















