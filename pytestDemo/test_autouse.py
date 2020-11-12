import time

import pytest


DATA_FORMAT='%Y-%m-%d %H:%M:%S'

@pytest.fixture(scope='session',autouse=True)
def temer_session_scope():
    start=time.time()
    print('\nstart:{}'.format(time.strftime(DATA_FORMAT,time.localtime(start))))
    yield
    finished=time.time()
    print('finished:{}'.format(time.strftime(DATA_FORMAT,time.localtime(finished))))
    print('total time cost:{:.3f}s'.format(finished-start))

@pytest.fixture(autouse=True)
def timer_function_scope():
    start=time.time()
    yield
    print('time cost:{:.3f}s'.format(time.time()-start))

def test_1():
    time.sleep(1)


def test_2():
    time.sleep(2)