import tkinter as tk
from tkinter import messagebox
from storage import load_users, save_users, load_games

users=load_users()
games=load_games()
current_user=None

def register():
 username= entry_username.get()
 password=entry_password.get()
 if not username or not password:
  messagebox.showerror("error", "Please enter username and password")
  return
 if username in users:
  messagebox.showerror("error","username exists")
  return
 users[username]={"password":password,"balance":50,"games":[]}
 save_users(users)
 messagebox.showinfo("Success",f"{username} registered")
 entry_username.delete(0,tk.END)
 entry_password.delete(0,tk.END)

def login():
 global current_user
 username=entry_username.get()
 password=entry_password.get()
 if username not in users or users[username]["password"]!=password:
  messagebox.showerror("error","Wrong username or password")
  return
 current_user=username
 messagebox.showinfo("Success",f"Logged in as {username}")
 entry_username.delete(0,tk.END)
 entry_password.delete(0,tk.END)

def logout():
 global current_user
 if current_user:
  current_user=None
  messagebox.showinfo("Info","Logged out successfully")
 else:
  messagebox.showinfo("Info","No user logged in")

def anonymous():
 global current_user
 current_user=None
 messagebox.showinfo("Info","Browsing anonymously")

def show_games():
 global current_user
 win=tk.Toplevel(root)
 win.title("Game Library")
 for g in games:
  frame=tk.Frame(win)
  frame.pack(fill="x",pady=2)
  info=f"{g['name']} - ${g['price']} | Tags: {', '.join(g['tags'])}"
  tk.Label(frame,text=info).pack(side="left")
  if current_user:
   tk.Button(frame,text="Buy",command=lambda game=g:buy_game(game)).pack(side="right")

def buy_game(game):
 global current_user
 if not current_user:
  messagebox.showinfo("info","Log in first to buy games")
  return
 user=users[current_user]
 if game["name"] in user["games"]:
  messagebox.showinfo("Info","error, you already own this game")
  return
 if user["balance"]<game["price"]:
  messagebox.showerror("error","not enough money")
  return
 user["balance"]-=game["price"]
 user["games"].append(game["name"])
 save_users(users)
 messagebox.showinfo("Success",f"Bought {game['name']}!")

root=tk.Tk()
root.title("My Game Library")
root.geometry("350x400")
root.configure(bg="#03fcec")

tk.Label(root,text="My Game Libary",font=("Monospaced",16,"bold"),bg="#03fcec").pack(pady=10)
tk.Label(root,text="Username",bg="#03fcec").pack()
entry_username=tk.Entry(root)
entry_username.pack()
tk.Label(root,text="Password",bg="#03fcec").pack()
entry_password=tk.Entry(root)
entry_password.pack()
tk.Button(root,text="Register",command=register).pack(pady=5)
tk.Button(root,text="Login",command=login).pack(pady=5)
tk.Button(root,text="Logout",command=logout).pack(pady=5)
tk.Button(root,text="Anonymous",command=anonymous).pack(pady=5)
tk.Button(root,text="Show Games",command=show_games).pack(pady=5)

root.mainloop()
