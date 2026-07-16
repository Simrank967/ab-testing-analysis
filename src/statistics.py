from statsmodels.stats.proportion import proportions_ztest
from scipy.stats import chi2_contingency
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize
import pandas as pd


def z_test(df):
    grouped = df.groupby("test group")["converted"]

    successes = grouped.sum()
    totals = grouped.count()

    z_stat, p_value = proportions_ztest(
        count=successes,
        nobs=totals
    )

    return z_stat, p_value


def chi_square_test(df):
    table = pd.crosstab(
        df["test group"],
        df["converted"]
    )

    chi2, p, dof, expected = chi2_contingency(table)

    return chi2, p


def sample_size_analysis(df):

    conversion = (
        df.groupby("test group")["converted"]
        .mean()
    )

    baseline = conversion.iloc[0]
    treatment = conversion.iloc[1]

    effect = proportion_effectsize(
        baseline,
        treatment
    )

    analysis = NormalIndPower()

    required = analysis.solve_power(
        effect_size=effect,
        alpha=0.05,
        power=0.80,
        ratio=1
    )

    actual = len(df)

    return required, actual

def calculate_lift(df):
    """
    Calculate control conversion rate, treatment conversion rate,
    absolute lift, and relative lift.
    """

    conversion = (
        df.groupby("test group")["converted"]
        .mean() * 100
    )

    # Get group names automatically
    groups = conversion.index.tolist()

    control_rate = conversion.iloc[0]
    treatment_rate = conversion.iloc[1]

    absolute_lift = treatment_rate - control_rate

    relative_lift = (
        (absolute_lift / control_rate) * 100
    )

    return {
        "control_group": groups[0],
        "treatment_group": groups[1],
        "control_rate": control_rate,
        "treatment_rate": treatment_rate,
        "absolute_lift": absolute_lift,
        "relative_lift": relative_lift
    }

import math

def confidence_interval(df):
    conversion = (
        df.groupby("test group")["converted"]
        .mean()
    )

    counts = (
        df.groupby("test group")["converted"]
        .count()
    )

    p1 = conversion.iloc[0]
    p2 = conversion.iloc[1]

    n1 = counts.iloc[0]
    n2 = counts.iloc[1]

    diff = p2 - p1

    se = math.sqrt(
        (p1 * (1 - p1) / n1) +
        (p2 * (1 - p2) / n2)
    )

    lower = diff - 1.96 * se
    upper = diff + 1.96 * se

    return lower * 100, upper * 100