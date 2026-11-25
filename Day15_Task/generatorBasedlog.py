

import os

# file path
script_folder = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(script_folder, "server.log")

# Create sample log file
with open(log_path, "w") as file:
    file.write("INFO: Server started\n")
    file.write("ERROR: Connection failed\n")
    file.write("INFO: User logged in\n")
    file.write("ERROR: Database error\n")
    file.write("WARNING: Low memory\n")
    file.write("ERROR: Connection failed\n")


# Generator function
def read_logs(filename):

    with open(filename, "r") as file:
        for line in file:
            yield line.strip()


error_count = {}

# Process logs
for log in read_logs(log_path):

    if "ERROR" in log:

        print("Error Found:", log)

        error_count[log] = error_count.get(log, 0) + 1


print("\nError Summary:")
print(error_count)