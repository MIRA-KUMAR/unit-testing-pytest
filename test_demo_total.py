from demo_total import total


def test_demo_total_empty():
    """To test if the fn returns 0.0 for an empty list"""
    assert total([]) == 0.0


def test_demo_total_single_element():
    """To test if an array with single item returns that item"""
    assert total([110]) == 110.0


def test_demo_total_many_elements():
    """To test if an array with many items returns their sum"""
    assert total([1.0, 2.0, 3.0, 4.0]) == 10.0
