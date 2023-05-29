# Ethical Hacking Goal

This repository contains a Python script that displays an ethical hacking goal as a GUI window. The script can be set up to run automatically every time you log in to Ubuntu.

## Prerequisites

- Python 3.x
- Tkinter (Python GUI library)

## Getting Started

1. Clone the repository to your local machine or download the script file (`ethical_hacking_goal.py`) directly.

2. Open a terminal and navigate to the directory where the `ethical_hacking_goal.py` script is located.

3. Install the necessary dependencies by running the following command: ```pip install tkinter```

4. Make sure the script is executable by running the following command: ```chmod +x goals.py```

5. Test the script by running the following command: ```python3 ethical_hacking_goal.py```

This will display the ethical hacking goal as a GUI window.

6. To run the script automatically on login, follow the steps below:

- Open a terminal and navigate to the `~/.config/autostart/` directory by running the following command:
  ```
  cd ~/.config/autostart/
  ```

- Create a new `.desktop` file using a text editor. For example, you can use the `vim` editor:
  ```
  vim ethical_hacking_goal.desktop
  ```

- In the text editor, paste the following content for the `.desktop` file:

  ```
  [Desktop Entry]
  Type=Application
  Exec=python3 /path/to/your/python/script.py
  Hidden=false
  NoDisplay=false
  X-GNOME-Autostart-enabled=true
  Name=Ethical Hacking Goal
  Comment=Run Ethical Hacking Goal script on startup
  ```

  Replace `/path/to/your/python/script.py` with the actual path to your Python script that contains the ethical hacking goal code.

- Save the file by pressing `Ctrl + O`, then exit the text editor by pressing `Ctrl + X`.

- Make the `.desktop` file executable by running the following command:
  ```
  chmod +x ethical_hacking_goal.desktop
  ```

7. Restart your Ubuntu system, and the ethical hacking goal script should now run automatically every time you log in.

## Customization

- If you want to customize the list of goals, you can modify the `goals` list in the `goals.py` script. Add or remove goals according to your preference.

- To customize the text colors or other styles of the GUI window, you can modify the respective sections in the `goals.py` script.

## License

This project is licensed under the ### <a href="#">[MIT License](LICENSE)</a>.
python3 goals.py
