from mypackage import myModule

def test_top_n():
    """
    Test the top_n function with a specific input and assert the expected output.

    """
    assert myModule.top_n([8,3,2,7,4], 3) == [8, 7, 4], 'incorrect'
    assert myModule.top_n([1, 2, 3, 4, 5], 2) == [5, 4], 'incorrect'
    assert myModule.top_n([5, 4, 3, 2, 1], 4) == [5, 4, 3, 2], 'incorrect'