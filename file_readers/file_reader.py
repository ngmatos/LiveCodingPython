class FileReader():
    def __init__(self, path):
        self.path = path

    def read_file(self):
        if self.path == None:
            return

        file = open(self.path)
        file_string = file.read()
        byte_array = bytes(file_string)
        return byte_array