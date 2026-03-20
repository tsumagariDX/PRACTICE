from pathlib import Path
import tkinter as tk

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

def on_add():
    print("追加ボタンが押されました")
    name = entry_name.get()
    price = entry_price.get()
    print(f'名前:{name},価格:{price}')
    
add_button = tk.Button(root, text="追加",command=on_add)
add_button.pack()



root.mainloop()

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

    while True:
        print("===商品管理アプリ===")
        print("1: 商品を追加")
        print("2: 商品一覧を見る")
        print("3: 商品を探す")
        print("4: 終了")
        print("5: 削除")
        print("6: 保存")
        print("7: 価格を変更")
        choice = input()

        if choice == "4": 
            app.save_to_file()
            print("保存して終了します") 
            break

        elif choice == "1":
            name = input("商品名を入力してください: ")
            price = (input("価格を入力してください: "))
            try:
                price = int(price)
            except:
                print("価格は数字で入力してください")
                continue

            result = app.add_product(name, price)
            if result:
                print("商品を追加しました")
            else:
                print("同じ名前の商品がすでにあります")

        elif choice == "2":
            app.show_products()

        elif choice == "3":
            name = input("探したい商品名を入力してください: ")
            product = app.find_product(name)

            if product is None:
                print("見つかりませんでした")
            else:
                print(f'見つかりました: 名前={product["name"]}, 価格={product["price"]}円')

        elif choice == "5":
            name = input("削除したい商品名を入力してください: ")
            result = app.remove_product(name)

            if result:
                print("削除しました")
            else:
                print("見つかりませんでした")

        elif choice == "6":
            app.save_to_file()
            print("保存しました")

        elif choice == "7":
            name = input("価格を変更したい商品名を入力してください")  
            new_price = input("変更後の価格を入力してください")
            try:
                new_price = int(new_price)
            except:
                print("価格は数字で入力してください")
                continue
            result = app.update_price(name, new_price)

            if result == False:
                print("見つかりませんでした")
            else:
                print(f"商品の価格を変更しました: 名前={name}, 価格={new_price}円")
