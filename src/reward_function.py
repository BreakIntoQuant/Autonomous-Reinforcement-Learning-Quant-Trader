def calculate_reward(
    pnl,
    drawdown_penalty=0
):

    reward = (
        pnl
        - drawdown_penalty
    )

    return reward