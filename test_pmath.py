import pytest
from pmath import Math

class TestMap:
    def setup_method(self):
        self.x = Math()
        print('start')

    def teardown_method(self):
        self.x = None
        print('end')

    @pytest.mark.parametrize(
        'a, b, expected',
        [
            (1, 2, 3),
            (3, 4, 7),
            (8, 7, 15),
            (6, 2, 8)
        ]
    )
    def test_add(self, a, b, expected):
        assert self.x.add(a, b) == expected

    def test_substract(self):
        assert self.x.substract(1, 5) == -4
