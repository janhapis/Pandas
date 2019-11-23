import pandas as pd
z = pd.read_csv('cars.csv')
x = z.loc[0:4]
a = x.loc[:,['Model','cyl','hp','wt','vs','gear']]
b = z.loc[z['Model'] == 'Mazda RX4',:]
c = z.loc[z['Model'] == 'Camaro Z28',['Model','cyl']]
d = z.loc[z['Model'].isin(['Mazda RX4 Wag','Ford Pantera L','Honda Civic']),['Model','cyl','gear']]