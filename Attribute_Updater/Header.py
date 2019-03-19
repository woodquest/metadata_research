class Header:
    def __init__(self):
        self.headers = ["h1", "h2", "h3", "h4"]

    def printheaders(self):
        print("printing the headers for this class")
        for header in self.headers:
            print("\t%s " % header)

