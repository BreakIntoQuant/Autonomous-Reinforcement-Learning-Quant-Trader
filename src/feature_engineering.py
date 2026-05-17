import pandas as pd
import numpy as np


def create_features(data):

    df = pd.DataFrame()

    df['Returns'] = (
        data['Close']
        .pct_change()
    )

    df['Momentum_5'] = (
        data['Close']
        / data['Close']
        .shift(5)
    )

    df['Momentum_20'] = (
        data['Close']
        / data['Close']
        .shift(20)
    )

    df['Volatility_20'] = (
        df['Returns']
        .rolling(20)
        .std()
    )

    df['SMA_20'] = (
        data['Close']
        .rolling(20)
        .mean()
    )

    df['SMA_50'] = (
        data['Close']
        .rolling(50)
        .mean()
    )

    df['RSI'] = calculate_rsi(
        data['Close']
    )

    return df.dropna()


def calculate_rsi(
    prices,
    period=14
):

    delta = prices.diff()

    gain = (
        delta.where(delta > 0, 0)
        .rolling(period)
        .mean()
    )

    loss = (
        -delta.where(delta < 0, 0)
        .rolling(period)
        .mean()
    )

    rs = gain / loss

    rsi = (
        100
        - (100 / (1 + rs))
    )

    return rsi