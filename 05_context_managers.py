class FileManager:

    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()


def main():

    filename = "sample.txt"

    with FileManager(filename, "w") as file:
        file.write("Learning Python Context Managers")

    with FileManager(filename, "r") as file:
        content = file.read()

    print("File Content:")
    print(content)


if __name__ == "__main__":
    main()
