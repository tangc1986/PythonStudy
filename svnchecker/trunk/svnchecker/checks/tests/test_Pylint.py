# pylint: disable-msg=W0232, W0603

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
Test methods for the Pylint class.
"""

from checks import Pylint
from tests.common import TestRepository, TestConfig

import os
import tempfile

configString = """
Pylint.IgnoreFiles=
"""

class TestPylint:

    @classmethod
    def setup_class(cls):
        handle, filename = tempfile.mkstemp()
        fd = os.fdopen(handle)
        fd.close()
        global configString
        # Test without pylintrc
        cls.configFilename, cls.config = TestConfig().createConfig(configString)
        # Test with pylintrc
        configString += "Pylint.ConfigFile=%s\n" % filename
        cls.configFilename2, cls.config2 = TestConfig().createConfig(configString)

    def testForSuccess(self):
        repository = TestRepository()
        repository.addFile("test.py", '""" docstring. """\nprint "hallo"')
        transaction = repository.commit()
        assert Pylint.run(transaction, self.config)[1] == 0
        assert Pylint.run(transaction, self.config2)[1] == 0

    def testForFailure(self):
        repository = TestRepository()
        repository.addFile("test.py", 'print "hallo"')
        transaction = repository.commit()
        assert Pylint.run(transaction, self.config)[1] == 1
        assert Pylint.run(transaction, self.config2)[1] == 1
