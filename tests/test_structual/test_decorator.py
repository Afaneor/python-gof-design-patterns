from patterns.structural.decorator import ExampleDecorator, ExampleSecondDecorator, SomeObject


def some_logic(some_object: SomeObject):
    some_object.some_logic()


def test_decorator():
    some_object = SomeObject()
    some_logic(some_object)

    decorator1 = ExampleDecorator(some_object)
    some_logic(decorator1)

    decorator2 = ExampleSecondDecorator(decorator1)
    some_logic(decorator2)
