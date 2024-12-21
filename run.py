from pymongo import MongoClient

# Підключення до MongoDB
client = MongoClient("mongodb://localhost:27017/")
#db = client["PetShop"]
db = client["violeta_lab"]


# Колекція
animals_collection = db["Animals"]

new_animal = {
    "AnimalID": 5,
    "Name": "Kesha",
    "Type": "Parrot",
    "Age": 3,
    "Price": 250.0
}

update_query = {"AnimalID": 5}
update_values = {"Name": "Kesha Updated", "Price": 275.0}  # Перейменовано з update_data

delete_query = {"AnimalID": 5}

# --- Меню ---
def menu():
    while True:
        print("\n--- Меню ---")
        print("1. Вивести всі дані")
        print("2. Додати дані")
        print("3. Оновити дані")
        print("4. Видалити дані")
        print("5. Вийти")
        
        choice = input("Оберіть пункт меню: ")
        
        if choice == "1":
            show_all_data()
        elif choice == "2":
            add_data()
        elif choice == "3":
            update_data()
        elif choice == "4":
            delete_data()
        elif choice == "5":
            print("Вихід...")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# --- CRUD функції ---
# 1. Вивести всі дані
def show_all_data():
    print("\n--- Всі дані ---")
    documents = animals_collection.find()
    for doc in documents:
        print(doc)

# 2. Додати дані
def add_data():
    print("\n--- Додати дані ---")
    try:
        animals_collection.insert_one(new_animal)
        print("Дані успішно додано:", new_animal)
    except Exception as e:
        print(f"Помилка: {e}")

# 3. Оновити дані
def update_data():
    print("\n--- Оновити дані ---")
    try:
        animals_collection.update_one(update_query, {"$set": update_values})
        print("Дані успішно оновлено:", update_values)
    except Exception as e:
        print(f"Помилка: {e}")

# 4. Видалити дані
def delete_data():
    print("\n--- Видалити дані ---")
    try:
        animals_collection.delete_one(delete_query)
        print("Дані успішно видалено:", delete_query)
    except Exception as e:
        print(f"Помилка: {e}")

# --- Запуск програми ---
if __name__ == "__main__":
    menu()