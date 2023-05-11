import pytest


class Tests5:

    @pytest.mark.group1  # it will run and at the same time it skipped also.
    @pytest.mark.skip
    def test_multi_008(self):
        x = 5
        y = 4
        multi = x * y

        if multi == 20:
            assert True
        else:
            assert False
