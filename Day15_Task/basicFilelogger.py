

import os

try:
    # The path of folder
    folder_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(folder_path, "user_logs.txt")

    with open(file_path, "a") as file:

        while True:
            log = input("Enter user action (type exit to stop): ")

            if log.lower() == "exit":
                break

            file.write(log + "\n")

    print("Logs saved successfully!")

except IOError:
    print("Error while accessing the file.")