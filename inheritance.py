class Phone:
    def call(self):
        print("Phone is called")

    def massage(self):
        print("Phone is massaged")


class Sumsung(Phone):  # use inheritance
    def photo(self):
        print("Photo is called")


s = Sumsung()
s.photo()
s.call()
s.massage()
print(issubclass(Sumsung, Phone))
