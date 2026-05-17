import matplotlib.pyplot as plt
import seaborn as sns


def plot_training_rewards(
    rewards
):

    plt.figure(figsize=(12, 6))

    plt.plot(rewards)

    plt.title(
        'Training Reward Curve'
    )

    plt.xlabel('Episode')

    plt.ylabel('Reward')

    plt.grid(True)

    plt.savefig(
        'charts/training_rewards.png'
    )

    print(
        "Training rewards saved."
    )


def plot_equity_curve(
    portfolio_values
):

    plt.figure(figsize=(12, 6))

    plt.plot(portfolio_values)

    plt.title(
        'RL Agent Equity Curve'
    )

    plt.grid(True)

    plt.savefig(
        'charts/equity_curve.png'
    )

    print(
        "Equity curve saved."
    )