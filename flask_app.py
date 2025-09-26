from flask import Flask, request, jsonify
from threading import Thread

app = Flask(__name__)

# In-memory users
users = {
    1: {"name": "Alice", "age": 25},
    2: {"name": "Bob", "age": 30}
}

# Flask routes
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    new_id = max(users.keys()) + 1 if users else 1
    users[new_id] = {"name": data["name"], "age": data["age"]}
    return jsonify({"id": new_id, "user": users[new_id]}), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    users[user_id].update(data)
    return jsonify(users[user_id])

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        deleted_user = users.pop(user_id)
        return jsonify({"deleted": deleted_user})
    return jsonify({"error": "User not found"}), 404

# Run Flask in a separate thread
def run_flask():
    app.run(debug=False)

# Start Flask server
Thread(target=run_flask).start()

# Console menu
while True:
    print("\n==== User Management Menu ====")
    print("1. View all users")
    print("2. View a user")
    print("3. Add a new user")
    print("4. Update a user")
    print("5. Delete a user")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("\nAll Users:")
        for uid, info in users.items():
            print(f"ID:{uid} Name:{info['name']} Age:{info['age']}")
    
    elif choice == "2":
        uid = int(input("Enter user ID: "))
        user = users.get(uid)
        if user:
            print(f"ID:{uid} Name:{user['name']} Age:{user['age']}")
        else:
            print("User not found!")
    
    elif choice == "3":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        new_id = max(users.keys()) + 1 if users else 1
        users[new_id] = {"name": name, "age": age}
        print(f"User added with ID {new_id}")
    
    elif choice == "4":
        uid = int(input("Enter user ID to update: "))
        if uid in users:
            name = input("Enter new name (leave blank to keep current): ")
            age_input = input("Enter new age (leave blank to keep current): ")
            if name:
                users[uid]['name'] = name
            if age_input:
                users[uid]['age'] = int(age_input)
            print("User updated successfully!")
        else:
            print("User not found!")
    
    elif choice == "5":
        uid = int(input("Enter user ID to delete: "))
        if uid in users:
            deleted = users.pop(uid)
            print(f"Deleted user: {deleted}")
        else:
            print("User not found!")
    
    elif choice == "6":
        print("Exiting...")
        break
    
    else:
        print("Invalid choice! Please enter 1-6.")
