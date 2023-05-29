import tkinter as tk
import datetime
import random

# List of goals to meetup with per day for the month of june
goals = [
    "Set up your ethical hacking environment.",
    "Learn the basics of networking.",
    "Familiarize yourself with \nLinux command-line basics.",
    "Today is Sunday so take a rest",
    "Study reconnaissance techniques.",
    "Dive into web application security.",
    "Practice password cracking techniques.",
    "Learn about wireless network security.",
    "Explore social engineering techniques.",
    "Delve into vulnerability \n scanning and assessment.",
    "Today is Sunday so take a rest",
    "Study exploit development.",
    "Practice secure coding practices.",
    "Learn about cryptography.",
    "Study forensic analysis techniques.",
    "Dive into mobile application security.",
    "Explore cloud security.",
    "Today is Sunday so take a rest",
    "Engage in a Capture The Flag (CTF) challenge.",
    "Study secure network \nconfiguration.",
    "Familiarize yourself with threat modeling\n and risk assessment methodologies.",
    "Learn about secure coding practices\n for web applications.",
    "Dive into reverse engineering.",
    "Practice conducting a penetration\n test on a target system.",
    "Today is Sunday so take a rest",
    "Study secure software development\n life cycle (SDLC) practices.",
    "Learn about secure coding practices\n for mobile applications.",
    "Study secure wireless network configurations.",
    "Familiarize yourself with incident \nresponse and handling procedures.",
    "Explore web server and application hardening\n techniques.",
    "Engage in a bug bounty program."
]

# Get the current day of the month
current_day = datetime.datetime.now().day

# Create the main window
root = tk.Tk()
root.configure(background="white")
root.attributes("-alpha", 0.9)  # Set transparency level


# Set the initial window size and position
window_width = root.winfo_screenwidth() // 4  # 25% of screen width
window_height = root.winfo_screenheight() // 10  # 10% of screen height
window_x = 0
window_y = root.winfo_screenheight() - window_height  # 10% of screen height
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


# Remove the title bar and the minimize, maximize, and exit icons
root.overrideredirect(True)

# Create the label with customized styles
label = tk.Button(
    root,
    text="Today's Goal",
    font=("Arial", 11),
    wraplength=400,
    relief=tk.FLAT,
    activebackground='black',
    activeforeground='white',
    fg='gold',  # Gold color
    bg='black'  # Black background
)
# label = tk.Label(root, text="Today's Goal", font=("Arial", 12, "bold"))
label.pack(pady=20)

# Function to change the text color randomly
def change_text_color():
    color = random.choice(["red", "green", "blue", "orange", "purple"])
    label.configure(fg=color)
    root.after(1000, change_text_color)

# Apply styles on hover
def on_enter(event):
    label.configure(fg=label["fg"])

def on_leave(event):
    label.configure(fg="black")

label.bind("<Enter>", on_enter)
label.bind("<Leave>", on_leave)

# Set the goal as label text
if 1 <= current_day <= len(goals):
    label["text"] = goals[current_day - 1]
else:
    label["text"] = "No goal for today."

# Start changing text color randomly
change_text_color()

# Run the GUI event loop
root.mainloop()

