from pathlib import Path
import tkinter as tk

class ProductList():
    def __init__(self):
        self.products = []

    def add_product(self,name,price): 
        found = self.find_product(name)
        if found:
            return False
        else:
            product = {"name": name, "price": price} 
            self.products.append(product)
            return True

    def show_products(self):
        if not self.products:
            print("商品がありません")
            return
        
        for product in self.products:
            print(f'名前:{product["name"]} / 価格: {product["price"]}円')

    def find_product(self,name):
        for product in self.products:
            if product["name"] == name:
                return(product)
        return None
    
    def remove_product(self,name):
        for product in self.products:
            if product["name"] == name:
                self.products.remove(product)
                return True
        return False
    
    def save_to_file(self):
        p = "products.txt"
        with open(p, "w", encoding="utf-8") as f:
            for product in self.products:
                f.write(f'{product["name"]},{product["price"]}\n')

    def load_from_file(self):
        p = Path("products.txt")
        if not p.exists():
            return
        
        self.products = []
        with open(p, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                parts = line.split(",")
                name = parts[0]
                price = int(parts[1])
                product = {"name": name, "price": price}
                self.products.append(product)

    def update_price(self, name, new_price):
        for product in self.products:
            if product["name"] == name:
                product["price"] = new_price
                return True
        return False

def main():
    app = ProductList()
    app.load_from_file()
    
    root = tk.Tk()
    root.title("ミニ商品管理アプリ")

    label_name = tk.Label(root, text = "商品名")
    label_name.pack()
    label_price = tk.Label(root, text = "価格")
    label_price.pack()

    entry_name = tk.Entry(root)
    entry_name.pack()
    entry_price = tk.Entry(root)
    entry_price.pack()

    listbox_products = tk.Listbox(root, width=40)
    listbox_products.pack()

    def get_price_from_entry():
        price = entry_price.get()
        try:
            price = int(price)
            return price
        except ValueError:
            print("価格は数字で入力してください")
            return None
        
    def get_name_from_entry():
        name = entry_name.get().strip()
        if name == "":
            print("商品名を入力してください")
            return None
        else:
            return name
    
    def refresh_listbox():
        listbox_products.delete(0,tk.END)
        for product in app.products:
            listbox_products.insert(tk.END,f'{product["name"]}/{product["price"]}円')

    def on_add():
        print("追加ボタンが押されました")
        name = get_name_from_entry()
        if name is None:
            return
        price = get_price_from_entry()
        if price is None:
            return
        
        result = app.add_product(name,price)

        if result:
            print("商品を追加しました")
            entry_name.delete(0,tk.END)
            entry_price.delete(0,tk.END)
        else:
            print("同じ名前の商品がすでにあります")
        print(f'名前:{name},価格:{price}')
        refresh_listbox()
    
    add_button = tk.Button(root, text="追加",command=on_add)
    add_button.pack()

    def on_delete():
        name = entry_name.get()
        result = app.remove_product(name)
        if result:
           print("削除しました")
           refresh_listbox()
        else:
            print("見つかりませんでした")

    del_button = tk.Button(root, text="削除", command=on_delete)
    del_button.pack()

    def on_update_price():
        name = entry_name.get()
        new_price = get_price_from_entry()
        if new_price is None:
            return
        
        result = app.update_price(name, new_price)

        if result:
            print("商品の価格を変更しました")
            refresh_listbox()
        else:
            print("商品が見つかりませんでした")
    
    up_button = tk.Button(root, text="価格変更", command=on_update_price)
    up_button.pack()

    def on_save():
        app.save_to_file()
        print("保存しました")
    sav_button = tk.Button(root, text="保存", command = on_save)
    sav_button.pack()

    def on_exit():
        on_save()
        root.destroy()
    ext_button = tk.Button(root, text="終了", command = on_exit)
    ext_button.pack()

    refresh_listbox()
    root.protocol("WM_DELETE_WINDOW", on_exit)
    root.mainloop()

if __name__ == "__main__":
    main()
