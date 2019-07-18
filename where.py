# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv("city/output/list_of_countries.csv")


def max_min_index(name_of_index):
    """Returns the maximum and minimum value of a column from df."""
    max_value = df[name_of_index].max()
    min_value = df[name_of_index].min()
    return max_value, min_value


max_min_purchasing = max_min_index('purchasing_power_index')
max_min_safety = max_min_index('safety_index')
max_min_health = max_min_index('health_care_index')
max_min_cost = max_min_index('cost_of_living_index')
max_min_property = max_min_index('property_price_to_income_ratio')
max_min_traffic = max_min_index('traffic_commute_time_index')
max_min_pollution = max_min_index('pollution_index')
max_min_climate = max_min_index('climate_index')

your_country = input("What is your country? ")
your_country = your_country.lower()
your_country = your_country.capitalize()

your_purchasing_power_index = float(
    df[df.country == your_country]["purchasing_power_index"]
)
print(f"In your country purchasing power index is {your_purchasing_power_index}")

your_purchasing_power_index = (
    float(input(f"What is your purchasing power index (higher is better)? "
                f"The best score in the world is "
                f"{max_min_purchasing[0]} "
                f"({list(df[df.purchasing_power_index == max_min_purchasing[0]]['country'])[0]}), "
                f"the worst is {max_min_purchasing[1]} "
                f"({list(df[df.purchasing_power_index == max_min_purchasing[1]]['country'])[0]}) ")) or
    your_purchasing_power_index
    )

your_safety_index = float(df[df.country == your_country]["safety_index"])
print(f"In your country safety index is {your_safety_index}")
your_safety_index = (
    float(input(f"What is your safety index (higher is better)? "
                f"The best score in the world is "
                f"{max_min_purchasing[0]} "
                f"({list(df[df.safety_index == max_min_safety[0]]['country'])[0]}), "
                f"the worst is {max_min_purchasing[1]} "
                f"({list(df[df.safety_index == max_min_safety[1]]['country'])[0]}) ")) or
    your_safety_index
)

your_health_care_index = float(df[df.country == your_country]["health_care_index"])
print(f"In your country health care index is {your_health_care_index}")
your_health_care_index = (
    float(input("What is your health care index (higher is better)? "
                f"The best score in the world is "
                f"{max_min_health[0]} "
                f"({list(df[df.health_care_index == max_min_health[0]]['country'])[0]}), "
                f"the worst is {max_min_health[1]} "
                f"({list(df[df.health_care_index == max_min_health[1]]['country'])[0]}) ")) or
    your_health_care_index
)

your_climate_index = float(df[df.country == your_country]["climate_index"])
print(f"In your country climate index is {your_climate_index}")
your_climate_index = (
    float(input("What is your climate index (higher is better)? "
                f"The best score in the world is "
                f"{max_min_climate[0]} "
                f"({list(df[df.climate_index == max_min_climate[0]]['country'])[0]}), "
                f"the worst is {max_min_climate[1]} "
                f"({list(df[df.climate_index == max_min_climate[1]]['country'])[0]}) ")) or
    your_climate_index
)

your_cost_of_living_index = float(
    df[df.country == your_country]["cost_of_living_index"]
)
print(f"In your country cost of living index is {your_cost_of_living_index}")
your_cost_of_living_index = (
    float(input("What is your cost of living index (lower is better)? "
                f"The best score in the world is "
                f"{max_min_cost[0]} "
                f"({list(df[df.cost_of_living_index == max_min_cost[0]]['country'])[0]}), "
                f"the worst is {max_min_cost[1]} "
                f"({list(df[df.cost_of_living_index == max_min_cost[1]]['country'])[0]}) ")) or
    your_cost_of_living_index
)

your_property_price_to_income_ratio = float(
    df[df.country == your_country]["property_price_to_income_ratio"]
)
print(
    f"In your country house "
    f"price to income ratio index is {your_property_price_to_income_ratio}"
)
your_property_price_to_income_ratio = (
    float(input("What is your house price to income ratio (lower is better)? "
                f"The best score in the world is "
                f"{max_min_property[0]} "
                f"({list(df[df.property_price_to_income_ratio == max_min_property[0]]['country'])[0]}), "
                f"the worst is {max_min_property[1]} "
                f"({list(df[df.property_price_to_income_ratio == max_min_property[1]]['country'])[0]}) ")) or
    your_property_price_to_income_ratio
)

your_traffic_commute_time_index = float(
    df[df.country == your_country]["traffic_commute_time_index"]
)
print(
    f"In your country traffic commute time index is {your_traffic_commute_time_index}"
)

your_traffic_commute_time_index = (
    float(input("What is your traffic commute time index (lower is better)? "
                f"The best score in the world is "
                f"{max_min_traffic[0]} "
                f"({list(df[df.traffic_commute_time_index == max_min_traffic[0]]['country'])[0]}), "
                f"the worst is {max_min_traffic[1]} "
                f"({list(df[df.traffic_commute_time_index == max_min_traffic[1]]['country'])[0]}) ")) or
    your_traffic_commute_time_index
)

your_pollution_index = float(df[df.country == your_country]["pollution_index"])
print(f"In your country pollution index is {your_pollution_index}")
your_pollution_index = (
    float(input("What is your pollution index (lower is better)? "
                f"The best score in the world is "
                f"{max_min_pollution[0]} "
                f"({list(df[df.pollution_index == max_min_pollution[0]]['country'])[0]}), "
                f"the worst is {max_min_pollution[1]} "
                f"({list(df[df.pollution_index == max_min_pollution[1]]['country'])[0]}) ")) or
    your_pollution_index
)

values = {
    "purchasing_power_index": 200,
    "safety_index": 200,
    "health_care_index": 200,
    "cost_of_living_index": 0,
    "property_price_to_income_ratio": 0,
    "traffic_commute_time_index": 0,
    "pollution_index": 0,
    "climate_index": 200,
}
df = df.fillna(value=values)

your_purchasing_power_index = float(your_purchasing_power_index)
your_safety_index = float(your_safety_index)
your_health_care_index = float(your_health_care_index)
your_cost_of_living_index = float(your_cost_of_living_index)
your_property_price_to_income_ratio = float(your_property_price_to_income_ratio)
your_traffic_commute_time_index = float(your_traffic_commute_time_index)
your_pollution_index = float(your_pollution_index)
your_climate_index = float(your_climate_index)

out_df = df[df.purchasing_power_index > your_purchasing_power_index][
    df.safety_index > your_safety_index
][df.health_care_index > your_health_care_index][
    df.cost_of_living_index < your_cost_of_living_index
][
    df.property_price_to_income_ratio < your_property_price_to_income_ratio
][
    df.traffic_commute_time_index < your_traffic_commute_time_index
][
    df.pollution_index < your_pollution_index
][
    df.climate_index > your_climate_index
]
print_out_df = out_df[["country", "freedomhouse_score", "quality_of_life_index"]]

if print_out_df.empty:
    print(f"Don't exist country better any {your_country}.")
else:
    with pd.option_context("display.max_rows", None, "display.max_columns", None):
        print(print_out_df)
