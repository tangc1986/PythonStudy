# pylint: disable-msg=E1101

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
Some global test settings and methods.
"""

import os
import py.test
import tempfile

from modules.Config import Config
from modules.Transaction import Transaction


class TestRepository:
    
    commitMessage = "MANTIS ID 1 MANTIS ID 2"
    
    def __init__(self):
        """ Create svn repository. """    
        self.repodir = tempfile.mkdtemp().replace("\\", "/")
        self.chkdir = tempfile.mkdtemp().replace("\\", "/")
        
        os.popen("svnadmin create %s" % self.repodir)
        os.popen("svn co file:///%s \"%s\"" % (self.repodir, self.chkdir))

    def createDefault(self):
        """ Creates the default repository content. """
        self.addFile("test 1.txt", "content")    
        self.setProperty("test 1.txt", "svn:keywords", "Date")
        self.addFile("test.java", "public interface test {\n}\n")
        self.commit(self.commitMessage)
        return self.repodir, Transaction(self.repodir, "1")

    def addFile(self, filename, content):
        """ Creates a new file in the repository. """
        fd = open(os.path.join(self.chkdir, filename), "w")
        fd.write(content)
        fd.close()
        os.popen("svn add \"%s\"" % os.path.join(self.chkdir, filename))
    
    def setProperty(self, filename, keyword, value):
        """ Sets a keywords on a file. """
        os.popen("svn propset %s %s \"%s\"" % (keyword, value, os.path.join(self.chkdir, filename)))

    def commit(self, commitMessage = ""):
        os.popen("svn commit -m \"%s\" %s" % (commitMessage, self.chkdir))
        return Transaction(self.repodir, "1")
    
    def createDiretory(self, path):
        os.mkdir(os.path.join(self.chkdir, path))
        os.popen("svn add \"%s\"" % os.path.join(self.chkdir, path))


class TestConfig:

    # To run the mantis tests you need to configure the options here.
    # You must have a three mantis ids, one and two assigned to you and marked in_progress    
    # and the third not assigned to anybody.

    mantisConfigString = """
Mantis.URL=xxx
Mantis.User=xxx
Mantis.Password=xxx
"""

    def __init__(self):
        """ Create the config file. """
        self.configFileHandle, self.configFilename = tempfile.mkstemp()

    def createConfig(self, content):
        """ Fill the config file with content. """
        content = "[Default]\n" + content

        fd = os.fdopen(self.configFileHandle, "w")
        fd.write(content)
        fd.close()

        return self.configFilename, Config(self.configFilename, self.configFilename)

    def createMantisConfig(self, content = ""):
        """ Create a mantis config file. """
        if "xxx" in self.mantisConfigString:
            py.test.skip("Please configure mantis access in common.py to run mantis tests.")
    
        return self.createConfig(self.mantisConfigString + "\n" + content)
