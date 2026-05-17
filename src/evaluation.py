import numpy as np


def calculate_sharpe_ratio(
    portfolio_values
):

    returns = (
        np.diff(portfolio_values)
        / portfolio_values[:-1]
    )

    if np.std(returns) == 0:

        return 0

    sharpe_ratio = (
        np.mean(returns)
        / np.std(returns)
    ) * np.sqrt(252)

    return sharpe_ratio


def calculate_max_drawdown(
    portfolio_values
):

    portfolio_values = np.array(
        portfolio_values
    )

    running_max = (
        np.maximum.accumulate(
            portfolio_values
        )
    )

    drawdowns = (
        portfolio_values
        / running_max
        - 1
    )

    return drawdowns.min()