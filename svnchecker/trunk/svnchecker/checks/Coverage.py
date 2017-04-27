# Copyright 2008 German Aerospace Center (DLR) # 
# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at #
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software 
# distributed under the License is distributed on an "AS IS" BASIS, 
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and 
# limitations under the License.

from __future__ import division
from modules import Process



def run(transaction, config):
    files = transaction.getFiles()

    for fileBase, attribute in files.iteritems():
        file = transaction.getFile(fileBase)
        Process.execute("coverage -x " + file)
        output = Process.execute("coverage -r " + file)
        output_list = output.split()
        ratio = int(output_list[6]) / int(output_list[7])
        configuredRatio = config.getInteger("Coverage.Ratio")
        if ratio > configuredRatio:
            return ("Too many uncovered statements in " +\
            fileBase.split("/")[1] + ". Your Ratio:" + str(ratio),1)

    return ("",0)
