from collections import deque
import random


class ReplayBuffer:

    def __init__(
        self,
        max_size=10000
    ):

        self.buffer = deque(
            maxlen=max_size
        )

    def add(
        self,
        experience
    ):

        self.buffer.append(
            experience
        )

    def sample(
        self,
        batch_size
    ):

        return random.sample(
            self.buffer,
            batch_size
        )