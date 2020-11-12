import pytest


@pytest.fixture()
def open_brower():
    print("打开浏览器")

    yield
    print("关闭浏览器")
@pytest.mark.usefixtures('open_brower')
def test_lookaround():
    print("登录后搜索")

def test_lookout():
    print("不登录查看")
@pytest.mark.usefixtures('open_brower')
def test_cart():
    print('登录，加购物车')

if __name__ =='__main__':
    pytest.main(['-v','test_fixture.py'])