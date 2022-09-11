from patterns.creational.singleton import SingletonExample


def test_singleton():
    object1 = SingletonExample()
    object2 = SingletonExample()
    assert object1 is object2
