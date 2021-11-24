


class tstyle:

    def __init__(self, text_color, font_size):
        #style attributes
        self.text_color = text_color;
        font_size = font_size;
        # many are there

    def get_details(self):
        print(f"for tag {__class__.__name__} : ")
        print(f"text_color = {__class__.text_color}")
        print(f"font_size = {__class__.font_size}")


class ttitle:

    def __init__(self):
        self.content ="";
        self.inner = []

    def get_details(self):
        print(f"for tag {__class__.__name__} : ")
        print(f"content = {self.content}")

class thead:

    def __init__(self):
        self.inner = []

    def tappend(self,tag):
        self.inner.append(tag)


class tp:

    def __init__(self):
        self.content = "";
        self.style =[];
        self.id = "";
        self.classs = [];
        self.inner = [];


    def tappend(self, tag):
        self.inner.append(tag)


class tdiv:

    def __init__(self):
        self.inner = [];
        self.style = [];
        self.id = "";
        self.classs = [];

    def tappend(self, tag):
        self.inner.append(tag)


class tbody:

    def __init__(self):
        self.inner = [];
        self.style = [];
        self.classs = [];

    def tappend(self, tag):
        self.inner.append(tag)


class thtml:

    def __init__(self):
        self.inner = []

    def tappend(self, tag):
        self.inner.append(tag)




