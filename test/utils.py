import os
from datetime import datetime

def create_test_file(directory, filename, content=""):
    filepath = os.path.join(directory, filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as file:
        file.write(content)
    # Set a fixed modification time for the file
    mod_time = datetime(2021, 1, 1).timestamp()
    os.utime(filepath, (mod_time, mod_time))