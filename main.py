import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Import ttk module for themed widgets
from PIL import Image, ImageTk


def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

def animateSnake():
    snake_canvas.create_image(50, 50, anchor='nw', image=snake_image)
    root.after(2000, clearCanvas)
    root.after(2000, evaluateResult)

def animateWater():
    water_canvas.create_image(50, 50, anchor='nw', image=water_image)
    root.after(2000, clearCanvas)
    root.after(2000, evaluateResult)

def animateGun():
    gun_canvas.create_image(50, 50, anchor='nw', image=gun_image)
    root.after(2000, clearCanvas)
    root.after(2000, evaluateResult)

def clearCanvas():
    snake_canvas.delete("all")
    water_canvas.delete("all")
    gun_canvas.delete("all")

def evaluateResult():
    comp_choice = computer_label.cget("text").split()[-1]
    user_choice = user_label.cget("text").split()[-1]

    result = gameWin(comp_choice, user_choice)

    if result == None:
        messagebox.showinfo("Result", "The game is a tie!")
    elif result:
        messagebox.showinfo("Result", "You Win!")
    else:
        messagebox.showinfo("Result", "You Lose!")



def play():
    comp_choices = ['s', 'w', 'g']
    comp = random.choice(comp_choices)
    user_choice = user_choice_var.get()

    if user_choice == 's':
        animateSnake()
    elif user_choice == 'w':
        animateWater()
    elif user_choice == 'g':
        animateGun()

    computer_label.config(text=f"Computer chose {comp}", font=("Helvetica", 14))
    user_label.config(text=f"You chose {user_choice}", font=("Helvetica", 14))




# GUI setup
root = tk.Tk()
root.title("Snake Water Gun Game")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate window size and animation size based on screen resolution
window_width = int(screen_width * 0.8)
window_height = int(screen_height * 0.8)
animation_size = int(window_width * 0.2)  # Adjust the size of animations as a percentage of the window width
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f'{window_width}x{window_height}+{x}+{y}')
root.attributes('-fullscreen', True)
user_choice_var = tk.StringVar()

choices = ['s', 'w', 'g']
# Labels
tk.Label(root, text="Snake Water Gun Game", font=("Helvetica", 20)).pack(pady=20)
tk.Label(root, text="Select your choice:", font=("Helvetica", 16)).pack()

# Radio Buttons
for choice in choices:
    tk.Radiobutton(root, text=choice, variable=user_choice_var, value=choice, font=("Helvetica", 14)).pack()

# Play button
play_button = tk.Button(root, text="Play", command=play, font=("Helvetica", 14))
play_button.pack(pady=20)

# Result labels
computer_label = tk.Label(root, text="", font=("Helvetica", 14))
computer_label.pack()

user_label = tk.Label(root, text="", font=("Helvetica", 14))
user_label.pack()

# Canvas for animations
snake_canvas = tk.Canvas(root, width=animation_size, height=animation_size)
snake_canvas.pack()

water_canvas = tk.Canvas(root, width=animation_size, height=animation_size)
water_canvas.pack()

gun_canvas = tk.Canvas(root, width=animation_size, height=animation_size)
gun_canvas.pack()

# Load animated GIFs and resize them
snake_image = Image.open('python project college tt\snake.gif').resize((animation_size, animation_size), Image.LANCZOS)
snake_image = ImageTk.PhotoImage(snake_image)

water_image = Image.open('python project college tt\Water.gif').resize((animation_size, animation_size), Image.LANCZOS)
water_image = ImageTk.PhotoImage(water_image)

gun_image = Image.open('python project college tt\gun.gif').resize((animation_size, animation_size), Image.LANCZOS)
gun_image = ImageTk.PhotoImage(gun_image)

# Create close, minimize, and maximize buttons using ttk module
close_button = ttk.Button(root, text="Close", command=root.destroy)
close_button.pack(side=tk.RIGHT, padx=10, pady=10)

minimize_button = ttk.Button(root, text="Minimize", command=root.iconify)
minimize_button.pack(side=tk.RIGHT, pady=10)

maximize_button = ttk.Button(root, text="Maximize", command=lambda: root.state('zoomed'))
maximize_button.pack(side=tk.RIGHT, pady=10)

root.mainloop()
