def train_agent(
    env,
    agent,
    episodes=50
):

    rewards = []

    for episode in range(episodes):

        state = env.reset()

        total_reward = 0

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

            total_reward += reward

            state = next_state

        agent.decay_epsilon()

        rewards.append(
            total_reward
        )

        print(
            f"Episode {episode+1}: "
            f"Reward = {total_reward:.2f}"
        )

    return rewards