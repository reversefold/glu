#
# Copyright 2010-2010 LinkedIn, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
#

import os
from setuptools import setup

setup(
  name             = "gluconsole",
  version          = "0.1",
  author           = "Manish Dubey",
  author_email     = "mdubey@linkedin.com",
  description      = ("GLU REST API"),
  install_requires = ['restkit', 'progressbar'],
  packages         = ['gluconsole'],
  scripts          =  ['src/cmdline/resources/bin/glu'],

  package_dir      = {
    'gluconsole': 'src/cmdline/resources/lib/python/gluconsole'
  },
)