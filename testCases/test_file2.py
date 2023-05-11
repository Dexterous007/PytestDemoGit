import pytest


class Test2:

    @pytest.mark.sanity    # collected 6 items / 4 deselected / 2 selected of sanity.
    def test_add_005(self):
        a = 10
        b = 50
        add = a+b
        print(add)

        if add == 60:
            assert True
        else:
            assert False
