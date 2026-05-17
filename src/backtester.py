def run_backtest(
    env,
    agent
):

    state = env.reset()

    done = False

    while not done:

        action = (
            agent.choose_action(
                state
            )
        )

        (
            next_state,
            reward,
            done
        ) = env.step(action)

        state = next_state

    return env.portfolio_values