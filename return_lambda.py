import pandas as pd
data = {'row_1':[3, 2, 1, 0], 'row_2':['a','b','c','d']}
y=pd.DataFrame(data)
x=pd.DataFrame.from_dict(data, orient='index')
print(y)
print(x)