# pylint: disable-msg=W0232, W0603

# Copyright 2008 Adam Byrtek
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
Test methods for the RejectTabs class.
"""

from checks import RejectTabs
from tests.common import TestRepository, TestConfig

import os
import tempfile

configString = """
RejectTabs.CheckFiles=.*\.py$
RejectTabs.IgnoreFiles=
"""

class TestRejectTabs:

    @classmethod
    def setup_class(cls):
        handle, filename = tempfile.mkstemp()
        fd = os.fdopen(handle)
        fd.close()
        global configString
        cls.configFilename, cls.config = TestConfig().createConfig(configString)

    def testRejectLeadingTabs(self):
        repository = TestRepository()
        repository.addFile("first_tab.py", 'if True:\n\tprint "Hello world"')
        repository.addFile("tab_after_space.py", 'if True:\n \tprint "Hello world"')
        repository.addFile("tab_inside.py", 'if True:    print "Hello\tworld"')
        transaction = repository.commit()

        msg, code = RejectTabs.run(transaction, self.config)
        msg_list = msg.split("\n")
        assert code == 1
        assert len(msg_list) == 2
        assert "File first_tab.py contains leading tabs" in msg_list
        assert "File tab_after_space.py contains leading tabs" in msg_list

    def testSkipBinaryFiles(self):
        repository = TestRepository()
        repository.addFile("binary_tab.py", '\t\t\t')
        repository.setProperty("binary_tab.py", "svn:mime-type", "application/octet-stream")
        transaction = repository.commit()

        msg, code = RejectTabs.run(transaction, self.config)
        assert code == 0

    def testIgnore(self):
        repository = TestRepository()
        repository.addFile("tabbed.txt", 'if True:\n\tprint "Hello world"')
        transaction = repository.commit()

        msg, code = RejectTabs.run(transaction, self.config)
        assert code == 0
