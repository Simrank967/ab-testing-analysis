import pandas as pd


def basic_summary(df):
    print("=" * 50)
    print("DATASET SHAPE")
    print("=" * 50)
    print(df.shape)

    print("\n" + "=" * 50)
    print("COLUMN TYPES")
    print("=" * 50)
    print(df.dtypes)

    print("\n" + "=" * 50)
    print("MISSING VALUES")
    print("=" * 50)
    print(df.isnull().sum())

    print("\n" + "=" * 50)
    print("NUMERICAL SUMMARY")
    print("=" * 50)
    print(df.describe())