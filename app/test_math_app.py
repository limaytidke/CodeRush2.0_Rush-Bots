from app.math_app import get_sorted_list

def test_get_sorted_list():
    result = get_sorted_list([3, 1, 4, 2])
    assert result == [1, 2, 3, 4], f"Expected [1, 2, 3, 4], but got {result}"