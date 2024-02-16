import csv
import pandas as pd
filename = './big-mac-full-index.csv'
df = pd.read_csv(filename)

print(df)

def get_big_mac_price_by_year(year,country_code):
    query = f"(iso_a3 == '{country_code.upper()}' and (date >= '{year}-01-01' and date <= '{year}-12-31'))"
    countrycode_df = df.query(query)

    return round(countrycode_df['dollar_price'].mean(), 2)

def get_big_mac_price_by_country(country_code):
    query = f"(iso_a3 == '{country_code.upper()}')"
    countrycode_df = df.query(query)

    return round(countrycode_df['dollar_price'].mean(),2)
    

def get_the_cheapest_big_mac_price_by_year(year):
    query = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    countrycode_df = df.query(query)

    min_idx = countrycode_df['dollar_price'].idxmin()
    country_name = countrycode_df.loc[min_idx]['name']
    country_code = countrycode_df.loc[min_idx]['iso_a3']
    dollar_price = countrycode_df.loc[min_idx]['dollar_price']

    return f"{country_name}({country_code}): ${round(dollar_price, 2)}"


def get_the_most_expensive_big_mac_price_by_year(year):
    query = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    countrycode_df = df.query(query)

    max_idx = countrycode_df['dollar_price'].idxmax()
    country_name = countrycode_df.loc[max_idx]['name']
    country_code = countrycode_df.loc[max_idx]['iso_a3']
    dollar_price = countrycode_df.loc[max_idx]['dollar_price']

    return f"{country_name}([{country_code}]): ${round(dollar_price,  2)}"

if __name__ == "__main__":
    print(2019, 'arg', get_big_mac_price_by_year(2019, 'arg'))
    print(2020, 'usa', get_big_mac_price_by_year(2020, 'usa'))
    print(2022, 'mex', get_big_mac_price_by_year(2022, 'mex'))
    
    print('arg', get_big_mac_price_by_country('arg'))
    print('usa', get_big_mac_price_by_country('usa'))
    print('mex', get_big_mac_price_by_country('mex'))

    print(2008, get_the_cheapest_big_mac_price_by_year(2008))
    print(2015, get_the_cheapest_big_mac_price_by_year(2015))
    print(2001, get_the_cheapest_big_mac_price_by_year(2001))

    print(2019, get_the_most_expensive_big_mac_price_by_year(2019))
    print(2020, get_the_most_expensive_big_mac_price_by_year(2020))
    print(2022, get_the_most_expensive_big_mac_price_by_year(2022))


