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

def show_report(item_sales, category_sales, top_item, top_category, skip_count):
    print("商品別売上: ")
    print()
    for item in item_sales:
        print(f"{item} : {item_sales[item]}")

    print("カテゴリ別売上: ")
    print()
    for category in category_sales:
        print(f"{category} : {category_sales[category]}")

    print("売上トップ商品: ")
    print(top_item)

    print("売上トップカテゴリ: ")
    print(top_category)

    print("スキップ件数: ")
    print()
    print(f"{skip_count} 件")

def save_report(output_path, item_sales, category_sales, top_item, top_category, skip_count):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("商品別売上: \n")
        for item in item_sales:
            f.write(f"{item} : {item_sales[item]}\n")
        f.write("カテゴリ別売上: \n")
        for category in category_sales:
            f.write(f"{category} : {category_sales[category]}\n")

        f.write("売上トップ商品: \n")
        f.write(f"{top_item}\n")

        f.write("売上トップカテゴリ: \n")
        f.write(f"{top_category}\n")

        f.write("スキップ件数: \n")
        f.write(f"{skip_count} 件\n")

def get_top_item(item_sales):
    max_price = 0
    max_price_item = ""
    for item in item_sales:
        if item_sales[item] > max_price:
            max_price = item_sales[item]
            max_price_item = item
    return  max_price_item

def sort_top_item(item_sales):
    sorted_top_item= {}
    for item in item_sales:
        sorted_top_item = sorted(item_sales.item(), key=lambda x: x[1], reverse=True)
    return sorted_top_item

def get_top_category(category_sales):
    max_sales = 0
    max_sales_category = ""
    for category in category_sales:
        if category_sales[category] > max_sales:
            max_sales = category_sales[category]
            max_sales_category = category
    return max_sales_category

def main():
    input_path = "sales.csv"
    output_path = "report.txt"

    records, skip_count = read_sales_csv(input_path)
    item_sales = calc_item_sales(records)
    category_sales = calc_category_sales(records)
    top_item = get_top_item(item_sales)
    top_category = get_top_category(category_sales)
    show_report(item_sales, category_sales, top_item, top_category, skip_count)
    save_report(output_path, item_sales, category_sales, top_item, top_category, skip_count)

if __name__ == "__main__":
    main()
