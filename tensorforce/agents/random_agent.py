# Copyright 2017 reinforce.io. All Rights Reserved.
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
# ==============================================================================

"""
Random agent that always returns a random action.
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import numpy as np

from tensorforce.agents import RLAgent
from tensorforce.util.experiment_util import global_seed


class RandomAgent(RLAgent):
    name = 'RandomAgent'

    def __init__(self, config, scope):
        super(RandomAgent, self).__init__()

        if config.deterministic_mode:
            self.random = global_seed()
        else:
            self.random = np.random.RandomState()

        self.actions = config.actions

    def get_action(self, state, episode=1):
        """
        Get random action from action space

        :param state: current state (disregarded)
        :param episode: episode number
        :return: random action
        """
        return self.random.randint(0, self.actions)

    def add_observation(self, *args, **kwargs):
        pass

    def load_model(self, *args, **kwargs):
        pass

    def save_model(self, *args, **kwargs):
        pass
