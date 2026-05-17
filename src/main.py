from data_loader import (
    download_data
)

from feature_engineering import (
    create_features
)

from trading_environment import (
    TradingEnvironment
)

from agent import (
    QLearningAgent
)

from training import (
    train_agent
)

from backtester import (
    run_backtest
)

from evaluation import (
    calculate_sharpe_ratio,
    calculate_max_drawdown
)

from visualization import (
    plot_training_rewards,
    plot_equity_curve
)


def main():

    ticker = "SPY"

    print(
        "\nDownloading market data..."
    )

    data = download_data(
        ticker,
        "2018-01-01",
        "2025-01-01"
    )

    print(
        "Engineering features..."
    )

    features = create_features(
        data
    )

    aligned_prices = (
        data['Close']
        .iloc[-len(features):]
    )

    print(
        "Initializing RL environment..."
    )

    env = TradingEnvironment(
        features,
        aligned_prices
    )

    agent = QLearningAgent()

    print(
        "Training reinforcement learning agent..."
    )

    rewards = train_agent(
        env,
        agent
    )

    print(
        "\nRunning backtest..."
    )

    portfolio_values = (
        run_backtest(
            env,
            agent
        )
    )

    sharpe_ratio = (
        calculate_sharpe_ratio(
            portfolio_values
        )
    )

    max_drawdown = (
        calculate_max_drawdown(
            portfolio_values
        )
    )

    print("\n==========")
    print("RL AGENT PERFORMANCE")
    print("==========")

    print(
        f"\nSharpe Ratio: {sharpe_ratio:.2f}"
    )

    print(
        f"Max Drawdown: {max_drawdown:.2%}"
    )

    print(
        "\nGenerating visualizations..."
    )

    plot_training_rewards(
        rewards
    )

    plot_equity_curve(
        portfolio_values
    )

    print(
        "\nAutonomous RL Trading Complete."
    )


if __name__ == "__main__":
    main()