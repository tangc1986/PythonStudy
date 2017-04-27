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
Test methods for the Console class.
"""

import os
import tempfile
import sys

from handlers import Console


class TestConsole:
    
    @classmethod
    def setup_class(cls):
        failureFileHandle, cls.failureFilename = tempfile.mkstemp()
        successFileHandle, cls.successFilename = tempfile.mkstemp()
        
        cls.failureFile = os.fdopen(failureFileHandle, "w")
        cls.successFile = os.fdopen(successFileHandle, "w")
        
        sys.stderr = cls.failureFile
        sys.stdout = cls.successFile
        
        cls.transaction = None
        cls.module = "dummy"
        cls.msg = "dummyMessage"
        cls.config = None
    
    def testRun(self):
        Console.run(self.transaction, self.config, self.module, self.msg, 1)
        Console.run(self.transaction, self.config, self.module, self.msg, 0)

        self.failureFile.close()
        self.successFile.close()

        fd = open(self.failureFilename, "r")
        content = fd.read()
        fd.close()
        assert content == Console.separator + self.msg + Console.separator

        fd = open(self.successFilename, "r")
        content = fd.read()
        fd.close()
        assert content == Console.separator + self.msg + Console.separator
