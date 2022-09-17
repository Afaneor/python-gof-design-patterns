import pytest

from patterns.structural.adapter import Adapter, Supported, Unsupported


def some_function(some_object: Supported):
    return some_object.some_method()


def test_adapter():
    test_object = Supported()

    test_object.some_method()

    unsupported = Unsupported()

    with pytest.raises(AttributeError):
        some_function(unsupported)

    adapter = Adapter(unsupported)

    some_function(adapter)
