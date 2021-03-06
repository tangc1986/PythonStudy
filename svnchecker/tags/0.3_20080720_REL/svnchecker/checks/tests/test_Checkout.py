# pylint: disable-msg=W0232

# Copyright 2008 German Aerospace Center (DLR)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Test methods for the Checkout class.
"""

import tempfile

from checks import Checkout
from tests.common import TestRepository, TestConfig


configString = """
Checkout.Entries=Entry1
Checkout.Entry1.Source=test.java
Checkout.Entry1.Destination=%DESTINATION%
"""

class TestCheckout:
    
    @classmethod
    def setup_class(cls):
        config = configString.replace("%DESTINATION%", tempfile.mkstemp()[1])
        cls.configFilename, cls.config = TestConfig().createConfig(config)
        cls.repository = TestRepository()
        cls.repodir, cls.transaction = cls.repository.createDefault()

    def testRun(self):
        assert Checkout.run(self.transaction, self.config)[1] == 0

