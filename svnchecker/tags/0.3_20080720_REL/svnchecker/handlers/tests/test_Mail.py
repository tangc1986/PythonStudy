# pylint: disable-msg=W0232, E1101

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
Test methods for the Mail class.
"""

import datetime
import py.test
import socket

from handlers import Mail
from tests.common import TestConfig, TestRepository


configString = """
Main.FailureAddresses=dummy@dummy.de
Main.SuccessAddresses=dummy@dummy.de
"""

class TestMail:
    
    @classmethod
    def setup_class(cls):
        cls.module = "dummy"
        cls.msg = "dummyMessage"
        cls.configFilename, cls.config = TestConfig().createConfig(configString)
        cls.repository = TestRepository()
        cls.repodir, cls.transaction = cls.repository.createDefault()
        cls.handler = Mail.MailHandler(cls.transaction, cls.config, cls.module, cls.msg)

    def testGetLogAddresses(self):
        assert self.handler.getLogAddresses() == ['dummy@dummy.de']

    def testGetErrorAddresses(self):
        assert self.handler.getErrorAddresses() == ['dummy@dummy.de']

    def testGetLogSubject(self):
        fromID = self.transaction.getUserID()
        assert self.handler.getLogSubject() == "SVN update by %s at %s" % (fromID, datetime.datetime.now().strftime("%H:%M - %d.%m.%Y"))

    def testGetErrorSubject(self):
        fromID = self.transaction.getUserID()
        assert self.handler.getErrorSubject() == "Checkin error by '%s' in check '%s'" % (fromID, self.module)

    def testCreateMail(self):
        fromAddress = "test@test.de"
        toAddress = "test2@test.de"
        subject = "asdf"
        content = "ab\nasf"
        assert self.handler.createMail(fromAddress, toAddress, subject, content) == \
            ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" % (fromAddress, toAddress, subject)) + content

    def testRun(self):
        # only runs if you have a local smtp server
        try:
            Mail.run(self.transaction, self.config, self.module, self.msg, 1)
            Mail.run(self.transaction, self.config, self.module, self.msg, 0)
        except socket.error:
            py.test.skip("You need a local smtp server to run this test.")
