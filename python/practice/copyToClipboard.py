import subprocess

def print_lines(file_path):
    page = 0
    with open(file_path, "r") as f:
        while True:
            chunks = ""
            for i in range(50):
                line = f.readline()
                if not line:
                    break
                chunks += line

            if not chunks:
                break

            subprocess.run("pbcopy", text=True, input=chunks)
            print(chunks)
            print("Page:", page)
            page += 1
            input("Press enter to continue...")

file_path = input("Enter file path: ")
print_lines(file_path)
