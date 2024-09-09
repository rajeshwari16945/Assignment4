import sqlite3
import tkinter

# Initialize the database
def init_db():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to add user data to the database
def add_user():
    name = entry_name.get()
    age = entry_age.get()

    if not name or not age:
        tkinter.messagebox.showwarning("Input Error", "Please provide both name and age.")
        return

    try:
        age = int(age)
    except ValueError:
        tkinter.messagebox.showwarning("Input Error", "Age must be an integer.")
        return

    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    conn.close()
    
    entry_name.delete(0, tkinter.END)
    entry_age.delete(0, tkinter.END)
    display_users()

# Function to display users in the listbox
def display_users():
    listbox_users.delete(0, tkinter.END)
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    
    for user in users:
        listbox_users.insert(tkinter.END, f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}")

# Initialize the main window
root = tkinter.Tk()
root.title("User Data Entry")

# Labels and Entry fields for the form
label_name = tkinter.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=10)

entry_name = tkinter.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_age = tkinter.Label(root, text="Age:")
label_age.grid(row=1, column=0, padx=10, pady=10)

entry_age = tkinter.Entry(root)
entry_age.grid(row=1, column=1, padx=10, pady=10)

# Button to submit the form
button_submit = tkinter.Button(root, text="Submit", command=add_user)
button_submit.grid(row=2, column=0, columnspan=2, pady=10)

# Listbox to display stored users
listbox_users = tkinter.Listbox(root, width=50)
listbox_users.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Initialize the database and display existing users
init_db()
display_users()

# Run the Tkinter main loop
root.mainloop()
