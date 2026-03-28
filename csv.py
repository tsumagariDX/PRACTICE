import csv

def read_work_log(input_path):
    with open(input_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)

        total_hours = 0
        skip_count = 0
        staff_hours = {}
        staff_costs = {}

        next(reader)
        for row in reader:

            if len(row) < 5:
                skip_count += 1
                continue

            staff = row[1]

            try:
                hours = int(row[3])
                rate = int(row[4])
            except ValueError:
                skip_count += 1
                continue

            total_hours += hours

            if staff not in staff_hours:
                staff_hours[staff] = 0
            staff_hours[staff] += hours

            if staff not in staff_costs:
                staff_costs[staff] = 0
            cost = hours * rate
            staff_costs[staff] += cost

        return total_hours, staff_hours, staff_costs, skip_count

def show_report(total_hours, staff_hours, staff_costs, skip_count):
    print(f"全体の作業時間合計: {total_hours}")
    print()

    print("スタッフ別作業時間:")
    for staff, hours in staff_hours.items():
        print(f"{staff}: {hours}")
    print()
    
    print("スタッフ別人件費:")
    for staff, cost in staff_costs.items():
        print(f"{staff}: {cost}")
    print()
    
    print(f"スキップ件数: {skip_count}")

def save_report(output_path, total_hours, staff_hours, staff_costs, skip_count):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"全体の作業時間合計: {total_hours}\n\n")

        f.write("スタッフ別作業時間:\n")
        for staff, hours in staff_hours.items():
            f.write(f"{staff}: {hours}\n")

        f.write(f"\nスタッフ別人件費:\n")
        for staff, cost in staff_costs.items():
            f.write(f"{staff}: {cost}\n")
        
        f.write(f"\nスキップ件数: {skip_count}")

def main():
    input_path = "work_log.csv"
    output_path = "report.txt"
    total_hours, staff_hours, staff_costs, skip_count = read_work_log(input_path)
    show_report(total_hours, staff_hours, staff_costs, skip_count)
    save_report(output_path, total_hours, staff_hours, staff_costs, skip_count)

main()
