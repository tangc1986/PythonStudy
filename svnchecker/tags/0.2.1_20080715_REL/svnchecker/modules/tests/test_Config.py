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
Test methods for the Config class.
"""

import os
import py.test
import tempfile

from modules.Config import Config, NoSuchConfigurationValueError

globalConfig = """
[Default]
Main.VarS=H
Resolving.VarT=G

[SubCat]
Main.regex=^/branch/
Main.VarU=F
Resolving.VarV=E
"""

localConfig = """
[Default]
Main.Checks=MantisCheck

Main.Java=/usr/bin/java

TestTest.BooleanA=1
TestTest.BooleanB=True
TestTest.BooleanC=true
TestTest.BooleanD=0
TestTest.BooleanE=False
TestTest.BooleanF=false
TestTest.List=a,b,c

Main.VarW=D
Resolving.VarX=C

[SubCat]
Main.regex=^/branch/
Main.VarY=B
Resolving.VarZ=A
Main.Hooks=%HOOKS%
"""

files = { '/branch/file.txt': 'A', '/branch/file2.txt' : 'A' }

class TestConfig:
    
    @classmethod
    def setup_class(cls):
        """ create example configurations. """
        handle, cls.globalConfigFilename = tempfile.mkstemp()
        fd = os.fdopen(handle, "w")
        fd.write(globalConfig)
        fd.close()
        
        handle, cls.localConfigFilename = tempfile.mkstemp()
        fd = os.fdopen(handle, "w")
        fd.write(localConfig)
        fd.close()
        
        cls.config = Config(cls.globalConfigFilename, cls.localConfigFilename)
        cls.config.setProfile("SubCat")
        
        cls.config.setHooksLocation("hooks")

    def testResolveOrder(self):
        assert self.config.getString("Resolving.VarZ") == "A"
        assert self.config.getString("Resolving.VarY") == "B"
        assert self.config.getString("Resolving.VarX") == "C"
        assert self.config.getString("Resolving.VarW") == "D"
        assert self.config.getString("Resolving.VarV") == "E"
        assert self.config.getString("Resolving.VarU") == "F"
        assert self.config.getString("Resolving.VarT") == "G"
        assert self.config.getString("Resolving.VarS") == "H"
        
        assert self.config.getString("Main.Hooks") == "hooks"
        
        py.test.raises(NoSuchConfigurationValueError, self.config.getString, "blablub.bla")
        py.test.raises(NoSuchConfigurationValueError, self.config.getString, "bla")
    
    def testGetBoolean(self):
        assert self.config.getBoolean("TestTest.BooleanA") == True
        assert self.config.getBoolean("TestTest.BooleanB") == True
        assert self.config.getBoolean("TestTest.BooleanC") == True
        assert self.config.getBoolean("TestTest.BooleanD") == False
        assert self.config.getBoolean("TestTest.BooleanE") == False
        assert self.config.getBoolean("TestTest.BooleanF") == False

    def testGetArray(self):
        assert self.config.getArray("TestTest.List") == ['a', 'b', 'c']
        