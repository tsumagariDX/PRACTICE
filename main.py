    def get_name_from_entry():
        name = entry_name.get().strip()
        if name == "":
            print("商品名を入力してください")
            return None
        else:
            return name
