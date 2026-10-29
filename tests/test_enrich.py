import pandas as pd
import pytest
from src.enrich import POPULATION

def calculate_rates(df: pd.DataFrame) -> pd.DataFrame:
    """Helper or refactored logic matching your enrichment math."""
    df["population"] = df["province"].map(POPULATION)
    df["mortality_rate_per_100k"] = ((df["deaths"] / df["population"]) * 100000).round(2)
    return df

def test_population_mapping():
    """Ensure known provinces map correctly to census populations."""
    assert POPULATION["western_cape"] == 7200000
    assert POPULATION["gauteng"] == 15000000

def test_mortality_rate_calculation():
    """Verify that per-capita mortality calculation produces correct values."""
    sample_data = pd.DataFrame({
        "province": ["western_cape", "gauteng"],
        "deaths": [720, 1500]
    })

    result = calculate_rates(sample_data)

    # 720 / 7,200,000 * 100,000 = 10.0
    # 1500 / 15,000,000 * 100,000 = 10.0
    assert result.loc[0, "mortality_rate_per_100k"] == 10.00
    assert result.loc[1, "mortality_rate_per_100k"] == 10.00

def test_missing_province_handling():
    """Provinces not in the dictionary should produce NaN for population."""
    sample_data = pd.DataFrame({
        "province": ["unknown_province"],
        "deaths": [50]
    })

    result = calculate_rates(sample_data)
    assert pd.isna(result.loc[0, "population"])
