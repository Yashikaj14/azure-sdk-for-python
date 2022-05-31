# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from typing import List

from ._operations import TestOperations as TestOperationsGenerated
class TestOperations(TestOperationsGenerated):
    def __init__(self, *args, **kwargs):
        #print(*args,**kwargs)
        super(TestOperations, self).__init__(*args, **kwargs)

    def upload_test_file():
        print("hello")
        return super().upload_test_file()



__all__: List[str] = ["TestOperations"]  # Add all objects you want publicly available to users at this package level

def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
