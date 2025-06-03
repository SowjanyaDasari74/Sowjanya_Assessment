initial_lines = ["First line", "Second line", "Third line"]

with open("file.txt", "w") as f:
    f.write("\n".join(initial_lines))

# Read the data from the file
with open("file.txt", "r") as f:
    content = f.readlines()
    print(f"Initial content of file.txt: {content}")

# Data to append
append_lines = ["Fourth line", "Fifth line", "Sixth line"]

# Append data to the file
with open("file.txt", "a") as f:
    for line in append_lines:
        f.write(line)
        f.write("\n")
f.seek(0)
# Read from the beginning of the file
with open("file.txt", "r") as f:
    updated_content = f.readlines()
    print(f"Updated content of file.txt: {updated_content}")
