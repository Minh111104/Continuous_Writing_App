# This is a simple tkinter app that force users to write continously. After 5 seconds of non-interaction, the app will delete all the text on the screen.
import tkinter as tk
import time
import threading
import random

# Function to clear the text after 5 seconds of non-interaction
def clear_text_after_delay():
    global last_interaction_time
    while True:
        current_time = time.time()
        if current_time - last_interaction_time > 5:
            text_widget.delete("1.0", tk.END)
            last_interaction_time = current_time
        time.sleep(1)

def on_key_press(event):
    global last_interaction_time
    last_interaction_time = time.time()  # Update the last interaction time on key press

def on_mouse_click(event):
    global last_interaction_time
    last_interaction_time = time.time()  # Update the last interaction time on mouse click

# Initialize the last interaction time
last_interaction_time = time.time()

# Start the thread to clear text after delay
clear_thread = threading.Thread(target=clear_text_after_delay, daemon=True)
clear_thread.start()

# Create the main application window
root = tk.Tk()
root.title("Continuous Writing App")
root.geometry("600x400")

# Create a frame for the countdown label at the top
top_frame = tk.Frame(root, bg="white")
top_frame.pack(fill=tk.X, side=tk.TOP)

# Countdown label to show time remaining (top-right corner)
countdown_var = tk.StringVar()
countdown_label = tk.Label(top_frame, textvariable=countdown_var, font=("Arial", 12), fg="red", bg="white")
countdown_label.pack(side=tk.RIGHT, padx=10, pady=2)

# Create a frame to hold the text widget
main_frame = tk.Frame(root)
main_frame.pack(expand=True, fill=tk.BOTH)

# Create a text widget for user input inside the frame
text_widget = tk.Text(main_frame, wrap=tk.WORD, font=("Arial", 14))
text_widget.pack(expand=True, fill=tk.BOTH)

# Countdown update function
def update_countdown():
    remaining = max(0, 5 - int(time.time() - last_interaction_time))
    countdown_var.set(f"Clearing in: {remaining}s")
    root.after(500, update_countdown)

update_countdown()  # Start the countdown update

# Bind key press and mouse click events to update last interaction time
text_widget.bind("<KeyPress>", on_key_press)
text_widget.bind("<Button-1>", on_mouse_click)

# Start the main event loop
root.mainloop()

