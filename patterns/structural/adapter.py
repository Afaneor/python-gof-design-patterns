class Supported(object):
    def some_method(self):
        pass


class Unsupported(object):
    def some_unsupported_method(self) -> str:
        pass


class Adapter(Supported):

    def __init__(self, unsupported_object: Unsupported):
        self.unsupported_object = unsupported_object

    def do_some_magic(self, string: str):
        pass

    def some_method(self):
        self.do_some_magic(self.unsupported_object.some_unsupported_method())
