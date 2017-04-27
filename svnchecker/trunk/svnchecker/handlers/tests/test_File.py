# pylint: disable-msg=W0603, W0232

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
Test methods for the File class.
"""

import os
import tempfile

from handlers import File
from tests.common import TestConfig


configString = """
Main.FailureFile=%FailureFile%
Main.SuccessFile=%SuccessFile%
"""

class TestFile:
    
    @classmethod
    def setup_class(cls):
        failureFileHandle, cls.failureFilename = tempfile.mkstemp()
        successFileHandle, cls.successFilename = tempfile.mkstemp()
        
        os.fdopen(failureFileHandle).close()
        os.fdopen(successFileHandle).close()
        
        global configString
        configString = configString.replace("%FailureFile%", cls.failureFilename)
        configString = configString.replace("%SuccessFile%", cls.successFilename)
        
        cls.transaction = None
        cls.module = "dummy"
        cls.msg = "dummyMessage"
        cls.configFilename, cls.config = TestConfig().createConfig(configString)
    
    def testRun(self):
        File.run(self.transaction, self.config, self.module, self.msg, 1)
        File.run(self.transaction, self.config, self.module, self.msg, 0)

        fd = open(self.failureFilename, "r")
        content = fd.read()
        fd.close()
        assert content == self.msg + File.separator

        fd = open(self.successFilename, "r")
        content = fd.read()
        fd.close()
        assert content == self.msg + File.separator

