class SomeObject(object):

    def some_logic(self):
        pass


class Decorator(SomeObject):

    _some_object: SomeObject

    def __init__(self, some_object: SomeObject):
        self._some_object = some_object

    def some_logic(self):
        self._some_object.some_logic()


class ExampleDecorator(Decorator):

    def some_logic(self):
        print('example')
        self._some_object.some_logic()


class ExampleSecondDecorator(Decorator):

    def some_logic(self):
        print('second example')
        self._some_object.some_logic()
