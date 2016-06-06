# Copyright 2016 Pavle Jonoski
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

__author__ = 'pavle'


class App:

    def __init__(self, name, description, command, tunnel_audio=False, tunnel_video=False):
        self.name = name
        self.description = description
        self.command = command
        self.tunnel_audio = tunnel_audio
        self.tunnel_video = tunnel_video
