import pytest


data1=['linda','seven']

@pytest.fixture()
def data(request):
    print("准备数据")
    return request.param

@pytest.mark.parametrize('data',data1,indirect=True)
def test_data(data):
    print(data)

if __name__ == '__main__':
    pytest.main(['-s','test_param_fixture.py'])