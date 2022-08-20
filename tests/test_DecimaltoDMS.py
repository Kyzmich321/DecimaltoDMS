from DecimaltoDMS import DecimaltoDMS
import pytest

cnt = 1


@pytest.fixture(autouse=True)
def func_fix():
    global cnt
    print(f"TEST {cnt}")
    cnt += 1


@pytest.mark.parametrize("a,result", [(-180, '180^0W'),
                                      (-180.0, "180^0W"),
                                      (0, '0^0E'),
                                      (180.0, "180^0E"),
                                      (180, '180^0E'),
                                      (170.0323, '170^1E'),
                                      (-13.912, "13^54W")])
def test_DecimaltoDMS_good(a,result):
    assert DecimaltoDMS(a) == result


