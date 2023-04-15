import matplotlib.pyplot as plot
plot.hist([10,10,10,5,5,5,5,5,3,4,4,8])
plot.show()

import pandas

data=pandas.read_excel("https://nasdaqbaltic.com/statistics/en/shares?download=1&date=2023-04-06")
print(data)