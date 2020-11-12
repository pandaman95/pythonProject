import pytest

test_user_data=["linda","seven"]

@pytest.fixture(params=test_user_data)
def login_r(request):
    user=request.param
    print("登录用户为：%s"% user)
    return user
def test_login_s(login_r):
    print(login_r)

if __name__=='__main__':
    pytest.main(['-s','test_fixtre_request.py'])