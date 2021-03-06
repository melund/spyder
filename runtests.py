# -*- coding: utf-8 -*-
#
# Copyright © 2009- The Spyder Development Team
# Licensed under the terms of the MIT License
#

"""
File for running tests programmatically.
"""

# Third party imports
import qtpy
import pytest


def main():
    """
    Run pytest tests.
    """
    pytest.main(['-x', 'spyderlib',  '-v', '-rw', '--durations=10',
                 '--cov=spyderlib', '--cov-report=term-missing'])


if __name__ == '__main__':
    main()
