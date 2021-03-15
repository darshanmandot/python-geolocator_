
from geopy.extra.rate_limiter import RateLimiter
import pandas as pd
from geopy.geocoders import ArcGIS


df = pd.read_csv("C:\\Users\\darsh\\Downloads\\us_address_sample.csv")


locator = ArcGIS(timeout=100)
geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
df['location'] = df['full_address'].apply(geocode)
df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)
df[['latitude', 'longitude']] = pd.DataFrame(df['point'].tolist(), index=df.index)
df = df.drop(['full_address', 'location','point'], axis=1)
df.to_csv('us_address_sample_update.csv')
