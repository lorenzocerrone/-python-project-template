# -*- coding: utf-8 -*-

"""
author: Lorenzo Cerrone
"""
from package_cool_name import main


class TestMain:
    def test_main(self):
        assert main.main() is None
