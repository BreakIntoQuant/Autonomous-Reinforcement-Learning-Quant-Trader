import numpy as np


class TradingEnvironment:

    def __init__(
        self,
        features,
        prices,
        initial_balance=100000
    ):

        self.features = (
            features.values
        )

        self.prices = (
            prices.values
        )

        self.initial_balance = (
            initial_balance
        )

        self.reset()

    def reset(self):

        self.current_step = 0

        self.balance = (
            self.initial_balance
        )

        self.position = 0

        self.portfolio_values = []

        return self.features[
            self.current_step
        ]

    def step(
        self,
        action
    ):

        current_price = (
            self.prices[
                self.current_step
            ]
        )

        previous_value = (
            self.balance
            + self.position
            * current_price
        )

        if action == 1:

            self.position += 1
            self.balance -= current_price

        elif action == 2:

            self.position -= 1
            self.balance += current_price

        self.current_step += 1

        done = (
            self.current_step
            >= len(self.features) - 1
        )

        next_price = (
            self.prices[
                self.current_step
            ]
        )

        current_value = (
            self.balance
            + self.position
            * next_price
        )

        reward = (
            current_value
            - previous_value
        )

        self.portfolio_values.append(
            current_value
        )

        next_state = (
            self.features[
                self.current_step
            ]
        )

        return (
            next_state,
            reward,
            done
        )