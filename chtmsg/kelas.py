class kelas:
    name = ""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''