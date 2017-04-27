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
Test methods for the Mantis class.
"""

from modules.Mantis import Mantis
from tests.common import TestConfig

class TestMantis:
    
    @classmethod
    def setup_class(cls):
        cls.configFilename, cls.config = TestConfig().createMantisConfig()
        cls.mantis = Mantis(cls.config)

    def testIssueExists(self):
        assert self.mantis.issueExists("1")
        assert self.mantis.issueExists("2")
        assert not self.mantis.issueExists("1111111111111111")

    def testIssueGetStatus(self):
        self.mantis.issueGetStatus("1")

    def testIssueGetHandler(self):
        self.mantis.issueGetHandler("1")
        self.mantis.issueGetHandler("2")

    def testIssueAddNote(self):
        self.mantis.issueAddNote("1", "test")
        
    def testIssueSetCustomFieldIfExists(self):
        self.mantis.issueSetCustomFieldIfExists("1", "SVNRevision", "123")
