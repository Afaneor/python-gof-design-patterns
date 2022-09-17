class SomeClass(object):

    def some_method(self):
        pass


class SomeClass2(object):

    def some_method2(self):
        pass


class Facade(object):

    def __init__(self, some_object=None, some_object2=None):
        self._some_object = some_object or SomeClass()
        self._some_object2 = some_object2 or SomeClass2()

    def do_magic(self):
        self._some_object.some_method()
        self._some_object2.some_method2()
