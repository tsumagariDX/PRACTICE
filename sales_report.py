import csv

def read_sales_csv(input_path):
    records = []
    skip_count = 0

    with open(input_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:

            if len(row) < 5:
                skip_count += 1
                continue
            try:
                quantity = int(row[3])
                price = int(row[4])
            except ValueError:
                skip_count += 1
                continue

            record = {
                "date": row[0],
                "item": row[1],
                "category": row[2],
                "quantity": quantity,
                "price": price
            }

            records.append(record)

    return records, skip_count

def calc_item_sales(records):
    item_sales = {}

    for record in records:
        item = record["item"]
        amount = record["quantity"] * record["price"]

        if item not in item_sales:
            item_sales[item] = 0
        
        item_sales[item] += amount
    
    return item_sales

def calc_category_sales(records):
    category_sales = {}

    for record in records:
        category = record["category"]
        amount = record["quantity"] * record["price"]

        if category not in category_sales:
            category_sales[category] = 0
        
        category_sales[category] += amount
    
    return category_sales

def show_report(item_sales, category_sales, skip_count):
    print("商品別売上: ")
    print()
    for item in item_sales:
        print(f"{item["item"]} : {item["amount"]}")

    print("カテゴリ別売上: ")
    print()
    for category in category_sales:
        print(f"{category["category"]} : {category["amount"]}")

    print("スキップ件数: ")
    print()
    print(f"{skip_count} 件")
