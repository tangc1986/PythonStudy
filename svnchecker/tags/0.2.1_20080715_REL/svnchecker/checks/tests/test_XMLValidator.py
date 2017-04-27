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
Test methods for the XMLValidator class.
"""

from checks import XMLValidator
from tests.common import TestRepository, TestConfig


configString = """
"""

class TestXMLValidator:
    
    @classmethod
    def setup_class(cls):
        cls.configFilename, cls.config = TestConfig().createConfig(configString)

    def testForSuccess(self):
        repository = TestRepository()
        repository.addFile("Test.xml", '<?xml version="1.0" encoding="UTF-8"?><body></body>')
        transaction = repository.commit()
        assert XMLValidator.run(transaction, self.config)[1] == 0

    def testForFailure(self):
        repository = TestRepository()
        repository.addFile("Test.xml", '<?xml version="1.0" encoding="UTF-8"?><body>/body>')
        transaction = repository.commit()
        assert XMLValidator.run(transaction, self.config)[1] == 1
