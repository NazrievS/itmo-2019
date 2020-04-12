# -*- coding: utf-8 -*-

import pytest   # noqa I001
import os   # noqa I001


dot = '.'
directory = 'directory'
test_file = 'example_file.py'
file_name = 'example.py'
date_time = '2019-02-07_07:51:24'


@pytest.fixture(params=[
    ('empty',
        [],
        [],
     ),
    ('dirsOnly',
        [directory],
        [directory],
     ),
    ('filesOnly',
        [test_file],
        [test_file],
     ),
    ('dirsAndFiles',
        [
            directory,
            test_file,
        ],
        [
            directory,
            test_file,
        ],
     ),
])
def ls_fixture(tmp_path, request):
    """Fixture for ls command."""
    first_param = request.param[0]
    path = tmp_path / first_param
    path.mkdir()
    for name in request.param[1]:
        element = path / name
        if dot in request.param[1]:
            element.join()
        else:
            element.mkdir()
    yield (path, request.param[2])


@pytest.fixture(params=[
    (file_name, True),
    ('имя.py', True),
    ('failure.py', False),
    ('example/.py', False),
])
def mk_fixture(request):
    """Fixture for mk command."""
    first_param = request.param[0]
    if first_param == 'failure.py':
        my_file = open(first_param, 'w+')  # noqa WPS515
        my_file.close()
    yield request.param
    if os.path.isfile(first_param):
        os.remove(first_param)


@pytest.fixture(params=[
    (file_name, True),
    (directory, False),
    ('example/.py', False),
])
def rm_fixture(tmp_path, request):
    """Fixture for rm command."""
    first_param = request.param[0]
    if dot in first_param:
        try:  # noqa WPS229
            my_file = open(first_param, 'w+')  # noqa WPS515
            my_file.close()
        except FileNotFoundError:
            pass  # noqa WPS420
    else:
        new_element = tmp_path / first_param
        new_element.mkdir()
    yield request.param


@pytest.fixture(params=[
    ('successfully.py', True),
    ('example/.py', False),
    (directory, False),
])
def contains_fixture(tmp_path, request):
    """Fixture for contains command."""
    first_param = request.param[0]
    if dot not in first_param:
        new_element = tmp_path / first_param
        new_element.mkdir()
    elif first_param == 'successfully.py':
        my_file = open(first_param, 'w+')  # noqa WPS515
        my_file.close()
    yield request.param
    if os.path.isfile(first_param):
        os.remove(first_param)


@pytest.fixture(params=[
    ('empty',
        date_time,
        [],
        [],
     ),
    ('dirsOnly',
        date_time,
        [directory],
        [directory],
     ),
    ('filesOnly',
        date_time,
        [test_file],
        [test_file],
     ),
    ('dirsAndFiles',
        date_time,
        [
            directory,
            test_file,
        ],
        [
            directory,
            test_file,
        ],
     ),
    ('wrongDate',
        '2020-02-0707:51:24',
        [test_file],
        'Using mask Y-M-D H:M:S',
     )])
def since_fixture(tmp_path, request):
    """Fixture for since command."""
    first_param = request.param[0]
    path = tmp_path / first_param
    path.mkdir()
    for name in request.param[2]:
        element = path / name
        if dot in request.param[2]:
            element.join()
        else:
            element.mkdir()
    yield (request.param[1], path, request.param[3])


@pytest.fixture(params=[
    ('ls', ''),
    ('mk', test_file),
    ('contains', test_file),
    ('since', date_time),
    ('rm', test_file),
])
def integration_fixture(request):
    """Fixture for integration tests."""
    yield request.param