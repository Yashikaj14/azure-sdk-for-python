# coding: utf-8
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import functools
from devtools_testutils import AzureTestCase, PowerShellPreparer
from azure.analytics.loadtestexample import LoadTestClient


class LoadtestexampleTest(AzureTestCase):
    def __init__(self, method_name, **kwargs):
        super(LoadtestexampleTest, self).__init__(method_name, **kwargs)

    def create_client(self, endpoint):
        credential = self.get_credential(LoadTestClient)
        return self.create_client_from_credential(
            LoadTestClient,
            credential=credential,
            endpoint=endpoint,
        )


LoadtestexamplePowerShellPreparer = functools.partial(
    PowerShellPreparer,
    "loadtestexample",
    loadtestexample_endpoint="https://myservice.azure.com"
)
