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
Test methods for the Process class.
"""

from modules import Process


class TestProcess:
    
    def testExecute(self):
        Process.execute("svnlook help")

        try:
            Process.execute("somecommand")
            assert False
        except Process.ProcessException, e:
            assert e.exitCode != 0
            assert e.command == "somecommand"
            assert e.output != ""
