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
Test methods for the UnitTests class.
"""

from checks import UnitTests
from tests.common import TestRepository, TestConfig


configString = """
"""

class TestUnitTests:
    
    @classmethod
    def setup_class(cls):
        cls.configFilename, cls.config = TestConfig().createConfig(configString)

    def testForSuccess(self):
        repository = TestRepository()
        repository.createDiretory("src")
        repository.createDiretory("src/main")
        repository.createDiretory("src/test")
        repository.addFile("src/main/Klasse.java", "public class Klasse {\n}\n")
        repository.addFile("src/test/KlasseTest.java", "public class TestKlasse {\n}\n")
        repository.addFile("TestInterface.java", "public interface TestInterface {\n}\n")
        transaction = repository.commit()
        assert UnitTests.run(transaction, self.config)[1] == 0

    def testForFailure(self):
        repository = TestRepository()
        repository.createDiretory("main")
        repository.addFile("main/Klasse.java", "public class Klasse {\n}\n")
        transaction = repository.commit()
        assert UnitTests.run(transaction, self.config)[1] == 1
