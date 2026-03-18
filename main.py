class ProductList():
    def __init__(self):
        self.products = []

    def add_product(self,name,price): 
        product = {"name": name, "price": price} 
        self.products.append(product)

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
def main():
    app = ProductList()
    while True:
        print("===商品管理アプリ===")
        print("1: 商品を追加")
        print("2: 商品一覧を見る")
        print("3: 商品を探す")
        print("4: 終了")
        print("5: 削除")
        choice = input()

        if choice == "4": 
            print("アプリを終了します") 
            break

        elif choice == "1":
            name = input("商品名を入力してください: ")
            price = int(input("価格を入力してください: "))
            app.add_product(name, price)
            print("商品を追加しました")

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
            product = app.remove_product(name)

            if product:
                print("削除しました")
            else:
                print("見つかりませんでした")

        