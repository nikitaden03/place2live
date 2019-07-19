import pytest
import pandas as pd


def max_min_index(name_of_index, name):
    """Returns the maximum and minimum value of a column from df."""
    max_value = df[name_of_index].max()
    max_country = list(df[name == max_value]['country'])
    min_value = df[name_of_index].min()
    min_country = list(df[name == min_value]['country'])
    return (max_value, max_country), (min_value, min_country)


df = pd.read_csv("city/output/list_of_countries.csv")


@pytest.mark.parametrize("name_index, name", [
    ('safety_index', df.safety_index),
    ('cost_of_living_index', df.cost_of_living_index),
    ('property_price_to_income_ratio', df.property_price_to_income_ratio),
    ('health_care_index', df.health_care_index),
    ('purchasing_power_index', df.purchasing_power_index),
    ('traffic_commute_time_index', df.traffic_commute_time_index),
    ('pollution_index', df.pollution_index),
])
def test_max_min_index(name_index, name):
    l = []
    for i in df[name_index]:
        if i != 'nan':
            l.append(i)
    max_value = max(l)
    min_value = min(l)
    max_country = list(df[name == max_value]['country'])
    min_country = list(df[name == min_value]['country'])
    b = max_min_index(name_index, name) == ((max_value, max_country),
                                            (min_value, min_country))
    if not b:
        raise AssertionError()
