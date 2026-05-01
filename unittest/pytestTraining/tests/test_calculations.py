import pytest

from src.calculations import Calculations
class TestCalculations:
    calc = Calculations()


    @pytest.mark.parametrize("n1, n2, exval",[(5, 5, 10),(-5, -5, -10),(0, 5, 5)])
    def test_add(self,n1, n2, exval):
        res = self.calc.add(n1, n2)
        assert res == exval, 'Add Err'

    @pytest.mark.parametrize("n1, n2, exval", [(5, 5, 0), (-5, -5, 0), (0, 5, -5)])
    def test_sub(self, n1, n2,exval):
        res = self.calc.sub(n1 , n2)
        assert res == exval, 'Sub Err'

    def test_mul(self):
        res = self.calc.mul(10, 5)
        assert res == 50, 'Mul Err'

    def test_div(self):
        res = self.calc.div(10, 5)
        assert res == 2.0, 'Div Err'

    def test_ne(self):
        res = self.calc.ne(10, 10)
        assert res == True, 'NE'

    @pytest.mark.xfail(reason='Excep not handle')
    def test_diverr(self):
        # with pytest.raises(ZeroDivisionError):
            self.calc.div(10, 0)

            res = self.calc.div(10, 10)
            assert res ==0
