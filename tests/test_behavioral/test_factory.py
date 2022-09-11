from patterns.creational.factory import Bake, CustomBake


def test_factory():
    # now we can hide logic of pastry behind bake
    pastry = Bake().create_pastry()
    custom_pastry = CustomBake().create_pastry()
    pastry.some_logic()
    custom_pastry.some_logic()
