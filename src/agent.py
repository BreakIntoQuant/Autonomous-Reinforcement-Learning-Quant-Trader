import numpy as np


class QLearningAgent:

    def __init__(
        self,
        action_space=3,
        epsilon=1.0,
        epsilon_decay=0.995,
        epsilon_min=0.01
    ):

        self.action_space = (
            action_space
        )

        self.epsilon = epsilon

        self.epsilon_decay = (
            epsilon_decay
        )

        self.epsilon_min = (
            epsilon_min
        )

    def choose_action(
        self,
        state
    ):

        if (
            np.random.rand()
            < self.epsilon
        ):

            return np.random.randint(
                self.action_space
            )

        return np.random.randint(
            self.action_space
        )

    def decay_epsilon(self):

        if (
            self.epsilon
            > self.epsilon_min
        ):

            self.epsilon *= (
                self.epsilon_decay
            )