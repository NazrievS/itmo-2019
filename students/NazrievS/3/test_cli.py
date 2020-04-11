# -*- coding: utf-8 -*-

import subprocess   # noqa: S404,I001

from cli import contains, ls    # noqa I001
from cli import mk, rm, since # noqa I001


def test_ls_execution(ls_fixture):
    """ls command test."""
    assert ls(ls_fixture[0]) == ls_fixture[1]


def test_mk_execution(mk_fixture):
    """mk command test."""
    assert mk(mk_fixture[0]) == mk_fixture[1]


def test_rm_execution(rm_fixture):
    """rm command test."""
    assert rm(rm_fixture[0]) == rm_fixture[1]


def test_contains_execution(contains_fixture):
    """contains command test."""
    assert contains(contains_fixture[0]) == contains_fixture[1]


def test_since_execution(since_fixture):
    """since command test."""
    assert since(
        since_fixture[0],
        since_fixture[1],
    ) == since_fixture[2]


def test_integration(integration_fixture):
    """Integration Tests."""
    command, args = integration_fixture
    callable_string = 'python students/NazrievS/3/cli.py {0} {1}'
    callable_string = callable_string.format(command, args)
    assert subprocess.call(callable_string, shell=True) == 0    # noqa: S602
