# pylint: disable-msg=W0232, E1101

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
Test methods for the CaseInsensitiveFilenameClash class.
"""

from checks import CaseInsensitiveFilenameClash
from tests.common import TestRepository, TestConfig

import py.test
import sys

configString = """
"""

class TestCaseInsensitiveFilenameClash:

    @classmethod
    def setup_class(cls):
        cls.configFilename, cls.config = TestConfig().createConfig(configString)

    def testForSuccess(self):
        repository = TestRepository()
        repository.createDiretory("src")
        repository.addFile("TestInterface.java", "public interface TestInterface {\n}\n")
        transaction = repository.commit()
        assert CaseInsensitiveFilenameClash.run(transaction, self.config)[1] == 0

    def testForFailure(self):
        if sys.platform == "win32":
            py.test.skip("This test only runs on *nix")

        repository = TestRepository()
        repository.createDiretory("main")
        repository.createDiretory("Main")
        transaction = repository.commit()
        assert CaseInsensitiveFilenameClash.run(transaction, self.config)[1] == 1
