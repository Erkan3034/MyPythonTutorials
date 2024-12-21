import tkinter as tk
from tkinter import messagebox
from market import *

class MarketApp:
    def __init__(self, root):
        self.market = Market()
        self.root = root
        self.root.title("Market Yönetim Sistemi")
        self.root.geometry("600x400")

        tk.Label(root, text="Market Programına Hoşgeldiniz", font=("Helvetica", 16)).pack(pady=10)

        tk.Button(root, text="Ürünleri Göster", command=self.list_products).pack(pady=5)
        tk.Button(root, text="Ürün Ekle", command=self.add_product_window).pack(pady=5)
        tk.Button(root, text="Ürün Sorgula", command=self.search_product_window).pack(pady=5)
        tk.Button(root, text="Ürün Sil", command=self.delete_product_window).pack(pady=5)
        tk.Button(root, text="Ürün Miktarını Arttır", command=self.increase_product_window).pack(pady=5)
        tk.Button(root, text="Çıkış", command=self.exit_app).pack(pady=5)

    def list_products(self):
        products = self.market.list_products()
        if not products:
            messagebox.showinfo("Ürünler", "Hiç ürün bulunamadı.")
        else:
            list_window = tk.Toplevel(self.root)
            list_window.title("Ürünler")
            for product in products:
                tk.Label(list_window, text=f"Ad: {product[0]}, ID: {product[1]}, Fiyat: {product[2]}, Miktar: {product[3]}").pack()

    def add_product_window(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Ürün Ekle")

        tk.Label(add_window, text="Ürün İsmi:").pack()
        name_entry = tk.Entry(add_window)
        name_entry.pack()

        tk.Label(add_window, text="Ürün ID:").pack()
        id_entry = tk.Entry(add_window)
        id_entry.pack()

        tk.Label(add_window, text="Ürün Fiyatı:").pack()
        price_entry = tk.Entry(add_window)
        price_entry.pack()

        tk.Label(add_window, text="Ürün Miktarı:").pack()
        amount_entry = tk.Entry(add_window)
        amount_entry.pack()

        def add_product():
            name = name_entry.get()
            id_ = int(id_entry.get())
            price = float(price_entry.get())
            amount = int(amount_entry.get())
            new_product = Product(name, id_, price, amount)
            self.market.add_product(new_product)
            messagebox.showinfo("Başarılı", "Ürün başarıyla eklendi.")
            add_window.destroy()

        tk.Button(add_window, text="Ekle", command=add_product).pack()

    def search_product_window(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Ürün Sorgula")

        tk.Label(search_window, text="Ürün İsmi:").pack()
        name_entry = tk.Entry(search_window)
        name_entry.pack()

        def search_product():
            name = name_entry.get()
            products = self.market.search_product(name)
            if products:
                for product in products:
                    messagebox.showinfo("Sonuç", f"Ad: {product[0]}, ID: {product[1]}, Fiyat: {product[2]}, Miktar: {product[3]}")
            else:
                messagebox.showinfo("Sonuç", "Ürün bulunamadı.")

        tk.Button(search_window, text="Sorgula", command=search_product).pack()

    def delete_product_window(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Ürün Sil")

        tk.Label(delete_window, text="Ürün İsmi:").pack()
        name_entry = tk.Entry(delete_window)
        name_entry.pack()

        def delete_product():
            name = name_entry.get()
            self.market.delete_product(name)
            messagebox.showinfo("Başarılı", "Ürün başarıyla silindi.")
            delete_window.destroy()

        tk.Button(delete_window, text="Sil", command=delete_product).pack()

    def increase_product_window(self):
        increase_window = tk.Toplevel(self.root)
        increase_window.title("Ürün Miktarını Arttır")

        tk.Label(increase_window, text="Ürün İsmi:").pack()
        name_entry = tk.Entry(increase_window)
        name_entry.pack()

        def increase_product():
            name = name_entry.get()
            if self.market.increase_amount(name):
                messagebox.showinfo("Başarılı", "Ürün miktarı başarıyla arttırıldı.")
            else:
                messagebox.showinfo("Hata", "Ürün bulunamadı.")
            increase_window.destroy()

        tk.Button(increase_window, text="Arttır", command=increase_product).pack()

    def exit_app(self):
        self.market.disconnect()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = MarketApp(root)
    root.mainloop()
