

def update_stock():
    print("\n--- inventory ---")
    name = input("Enter product name:").strip().lower()

    for item in inventory:
        if item["name"].lower() == name:
            print(f"Current stock for {item['name']}:{item['qty']}")
            new_qty = input("Enter new quantity:")

            try:
                item["qty"]=int(new_qty)
                print(f"Updated! {item['name']}is now {item['qty']}units.")
            except ValueError:
                print("Please enter a valid number.")
                return
            
        print(f"Product'{name}'")
        # Example inventory list 
inventory = [
            {"name":"apple", "qty":50, "price":0.5},
            {"name":"banana", "qty":30, "price":0.2},
            {"name":"berries", "qty":120, "price":0.8}
        ]        
print(f"{'Name':<10}{'Quantity':<10}{'Price':<10}")

for item in inventory:
    print(f"{item['name']:<10}{item['qty']:<10}{item['price']:<10}")

update_stock()
  


