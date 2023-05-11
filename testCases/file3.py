# This file will not identify by pytest because of filename. It will not Run.
# In this we didn't consider 'test_*'.py as prefix before filename(file3.py)

class Test3:

    def test_add_006(self):
        a = 10
        b = 70
        add = a+b
        print(add)

        if add == 80:
            assert True
        else:
            assert False
