# pylint: disable-msg=W0232, E1102

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
Test methods for the Transaction class.
"""

import py.test

from tests.common import TestRepository
from modules.Transaction import FileNotFoundException, PropertyNotFoundException


class TestTransaction:
    
    @classmethod
    def setup_class(cls):
        """ create reference to transaction. """
        cls.repository = TestRepository()
        cls.repodir, cls.transaction = cls.repository.createDefault()
        
    def testGetUserID(self):
        assert self.transaction.getUserID()

    def testGetFiles(self):
        assert self.transaction.getFiles() == { 'test.java' : 'A', 'test 1.txt' : 'A' }
        assert self.transaction.getFiles([".*\.java"]) == { 'test.java' : 'A' }
        assert self.transaction.getFiles([".*"], [".*\.java"]) == { 'test 1.txt' : 'A' }
        assert self.transaction.getFiles(["test.java", "test 1.txt"]) == { 'test.java' : 'A', 'test 1.txt' : 'A' }
        assert self.transaction.getFiles(["test.java", "test 1.txt"], ["test.java"]) == { 'test 1.txt' : 'A' }
        
    def testGetFile(self):
        filename = self.transaction.getFile("test 1.txt")
        assert open(filename).read() == "content"
        # Test caching
        filename = self.transaction.getFile("test 1.txt")
        assert open(filename).read() == "content"
        py.test.raises(FileNotFoundException, self.transaction.getFile, "blablub")

    def testFileExists(self):
        assert self.transaction.fileExists("test 1.txt")
        assert not self.transaction.fileExists("bla.txt")

    def testGetCommitMsg(self):
        assert self.transaction.getCommitMsg() == self.repository.commitMessage
    
    def testGetRevision(self):
        assert self.transaction.getRevision() == "1"
    
    def testHasProperty(self):
        assert self.transaction.hasProperty("svn:keywords", "test 1.txt")
        py.test.raises(FileNotFoundException, self.transaction.getProperty, "keywordx", "bla")
        assert not self.transaction.hasProperty("keywordx", "test 1.txt")
    
    def testGetKeyword(self):
        assert self.transaction.getProperty("svn:keywords", "test 1.txt") == "Date"
        py.test.raises(FileNotFoundException, self.transaction.getProperty, "keywordx", "bla")
        py.test.raises(PropertyNotFoundException, self.transaction.getProperty, "keywordx", "test 1.txt")

    def testListKeywords(self):
        assert self.transaction.listProperties("test 1.txt") == ["svn:keywords"]
        assert self.transaction.listProperties("test.java") == []
        py.test.raises(FileNotFoundException, self.transaction.listProperties, "bla")
        