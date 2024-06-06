class Phone:
    def __init__(self):
        print("i am phone class")


class Email(Phone):

    def __init__(self):
        super().__init__()  # super class added
        print("i am email class")


e = Email()
