from patterns.creational.builder import Builder


def test_builder():
    builder = Builder()
    builder.create_test_product()
    product1 = builder.product

    builder.create_part_a()
    product2 = builder.product

    assert product1 is not product2
