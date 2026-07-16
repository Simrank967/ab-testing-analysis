import pandas as pd

from src.database import create_database, run_query
from src.analysis import basic_summary

from src.statistics import (
    z_test,
    chi_square_test,
    sample_size_analysis,
    calculate_lift,
    confidence_interval
)

from src.visualization import (
    plot_conversion_rate,
    plot_ads_day,
    plot_ads_hour,
    plot_segment_analysis
)

from src.report import generate_report


# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv("data/marketing_AB.csv")

if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])


# ==========================================
# EDA
# ==========================================

basic_summary(df)


# ==========================================
# CREATE SQLITE DATABASE
# ==========================================

create_database()


# ==========================================
# SQL ANALYSIS
# ==========================================

print("\n")
print("=" * 50)
print("CONVERSION RATE")
print("=" * 50)

conversion = run_query("sql/conversion_rate.sql")
print(conversion)

print("\n")
print("=" * 50)
print("DAY ANALYSIS")
print("=" * 50)

day = run_query("sql/day_analysis.sql")
print(day)

print("\n")
print("=" * 50)
print("HOUR ANALYSIS")
print("=" * 50)

hour = run_query("sql/hour_analysis.sql")
print(hour)


# ==========================================
# USER SEGMENT ANALYSIS
# ==========================================

print("\n")
print("=" * 60)
print("USER SEGMENT ANALYSIS")
print("=" * 60)

segment = run_query("sql/segment_analysis.sql")

print(segment)


# ==========================================
# VISUALIZATIONS
# ==========================================

plot_conversion_rate(df)
plot_ads_day(df)
plot_ads_hour(df)
plot_segment_analysis(segment)

print("\nCharts saved successfully in outputs/")


# ==========================================
# STATISTICAL ANALYSIS
# ==========================================

print("\n")
print("=" * 50)
print("STATISTICAL ANALYSIS")
print("=" * 50)

z, p = z_test(df)

print(f"Z Statistic : {z:.4f}")
print(f"P Value     : {p:.2e}")

chi2, chi_p = chi_square_test(df)

print(f"\nChi Square  : {chi2:.4f}")
print(f"P Value     : {chi_p:.2e}")


# ==========================================
# SAMPLE SIZE
# ==========================================

required, actual = sample_size_analysis(df)

print("\n")
print("=" * 50)
print("SAMPLE SIZE")
print("=" * 50)

print(f"Required Sample : {required:.0f}")
print(f"Actual Sample   : {actual}")


# ==========================================
# LIFT ANALYSIS
# ==========================================

print("\n")
print("=" * 50)
print("LIFT ANALYSIS")
print("=" * 50)

lift = calculate_lift(df)

print(f"Control Group        : {lift['control_group']}")
print(f"Treatment Group      : {lift['treatment_group']}")

print(f"\nControl Conversion   : {lift['control_rate']:.2f}%")
print(f"Treatment Conversion : {lift['treatment_rate']:.2f}%")

print(f"\nAbsolute Lift        : {lift['absolute_lift']:.2f}%")
print(f"Relative Lift        : {lift['relative_lift']:.2f}%")


# ==========================================
# CONFIDENCE INTERVAL
# ==========================================

lower, upper = confidence_interval(df)

print("\n")
print("=" * 50)
print("95% CONFIDENCE INTERVAL")
print("=" * 50)

print(f"Lower Bound : {lower:.2f}%")
print(f"Upper Bound : {upper:.2f}%")


# ==========================================
# GENERATE FINAL REPORT
# ==========================================

generate_report(
    lift,
    p,
    chi_p,
    required,
    actual
)

print("\nReport saved successfully in outputs/recommendation.txt")