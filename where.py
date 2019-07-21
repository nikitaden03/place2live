# -*- coding: utf-8 -*-
import pandas as pd


def max_min_index(name_index, df):
    """Return maximum and minimum value with country of a column from df."""
    country_and_name = df[['country', name_index]]
    counrties_in_name_index = country_and_name.sort_values(name_index).dropna()
    min_value = [list(counrties_in_name_index[name_index])[0],
                 list(counrties_in_name_index['country'])[0]]
    max_value = [list(counrties_in_name_index[name_index])[-1],
                 list(counrties_in_name_index['country'])[-1]]
    return max_value, min_value


def print_question(name_index, max_min_value, mood):
    """
    Return a question that asks the user about the status of a factor
    in his country, also displays the maximum and minimum value of this factor
    in the world.
    """
    if mood == 'higher is better':
        first_value = max_min_value[0]
        second_value = max_min_value[1]
    elif mood == 'lower is better':
        first_value = max_min_value[1]
        second_value = max_min_value[0]
    message = (
        f"What is your desirable {name_index} ({mood})? "
        f"The best score in the world is "
        f"{first_value[0]} "
        f"({first_value[1]}), "
        f"the worst is {second_value[0]} "
        f"({second_value[1]}) "
    )
    return message


def main():
    df = pd.read_csv("city/output/list_of_countries.csv")
    max_min_purchasing = max_min_index('purchasing_power_index', df)
    max_min_safety = max_min_index('safety_index', df)
    max_min_health = max_min_index('health_care_index', df)
    max_min_cost = max_min_index('cost_of_living_index', df)
    max_min_property = max_min_index('property_price_to_income_ratio', df)
    max_min_traffic = max_min_index('traffic_commute_time_index', df)
    max_min_pollution = max_min_index('pollution_index', df)
    max_min_climate = max_min_index('climate_index', df)

    your_country = input("What is your country? ")
    your_country = your_country.lower()
    your_country = your_country.capitalize()

    your_purchasing_power_index = float(
        df[df.country == your_country]["purchasing_power_index"]
    )
    print(
        f"In your country purchasing power index is "
        f"{your_purchasing_power_index}"
        )
    your_purchasing_power_index = (
        float(input(
            print_question('purchasing power index', max_min_purchasing,
                           'higher is better')
        )) or
        your_purchasing_power_index
        )

    your_safety_index = float(
        df[df.country == your_country]["safety_index"]
    )
    print(f"In your country safety index is {your_safety_index}")
    your_safety_index = (
        float(input(
            print_question('safety index', max_min_safety, 'higher is better')
        )) or
        your_safety_index
    )

    your_health_care_index = float(
        df[df.country == your_country]["health_care_index"]
    )
    print(f"In your country health care index is {your_health_care_index}")
    your_health_care_index = (
        float(input(
            print_question('health care index', max_min_health,
                           mood='higher is better')
        )) or
        your_health_care_index
    )

    your_climate_index = float(
        df[df.country == your_country]["climate_index"]
    )
    print(f"In your country climate index is {your_climate_index}")
    your_climate_index = (
        float(input(
            print_question('climate index', max_min_climate,
                           'higher is better')
        )) or
        your_climate_index
    )

    your_cost_of_living_index = float(
        df[df.country == your_country]["cost_of_living_index"]
    )
    print(f"In your country cost of living index is "
          f"{your_cost_of_living_index}")
    your_cost_of_living_index = (
        float(input(
            print_question('cost of living index', max_min_cost,
                           'lower is better')
        )) or
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
        float(input(
            print_question('property price to income ratio', max_min_property,
                           'lower is better')
        )) or
        your_property_price_to_income_ratio
    )

    your_traffic_commute_time_index = float(
        df[df.country == your_country]["traffic_commute_time_index"]
    )
    print(
        f"In your country traffic commute time index is "
        f"{your_traffic_commute_time_index}"
    )
    your_traffic_commute_time_index = (
        float(input(
            print_question('traffic commute time index', max_min_traffic,
                           'lower is better')
        )) or
        your_traffic_commute_time_index
    )

    your_pollution_index = float(
        df[df.country == your_country]["pollution_index"]
        )
    print(f"In your country pollution index is {your_pollution_index}")
    your_pollution_index = (
        float(input(
            print_question('pollution index', max_min_pollution,
                           'lower is better')
        )) or
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
    your_property_price_to_income_ratio = float(
        your_property_price_to_income_ratio
        )
    your_traffic_commute_time_index = float(your_traffic_commute_time_index)
    your_pollution_index = float(your_pollution_index)
    your_climate_index = float(your_climate_index)
    out_df = df[(df.purchasing_power_index > your_purchasing_power_index) &
                (df.safety_index > your_safety_index) &
                (df.health_care_index > your_health_care_index) &
                (df.cost_of_living_index < your_cost_of_living_index) &
                (df.property_price_to_income_ratio <
                    your_property_price_to_income_ratio) &
                (df.traffic_commute_time_index <
                    your_traffic_commute_time_index) &
                (df.pollution_index < your_pollution_index) &
                (df.climate_index > your_climate_index)]

    print_out_df = out_df[
        ["country", "freedomhouse_score", "quality_of_life_index"]
    ].dropna().sort_values(by=['freedomhouse_score'],
                           ascending=False)

    if print_out_df.empty:
        print(f"There is no country better than {your_country}.")
    else:
        with pd.option_context("display.max_rows", None, "display.max_columns",
                               None):
            print(print_out_df)


if __name__ == '__main__':
    main()
