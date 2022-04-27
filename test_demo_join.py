from demo_join import join


def test_demo_join_usecase1():
    assert join([1, 2, 3], ", ") == '1, 2, 3'


def test_demo_join_usecase2():
    assert join([1], "") == '1'


def test_demo_join_usecase3():
    assert join([], "") == ""


def test_demo_join_usecase4():
    assert join([4, 5, 6], "+ ") == '4+ 5+ 6'


def test_demo_join_usecase5():
    assert join([1, 2, 3], "") == '123'
