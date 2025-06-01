import pandas as pd
from ydata_profiling import ProfileReport

df=pd.read_csv('diabetes1.csv')

profile =ProfileReport(df)
profile.to_file(output_file="charts.htmlpip ")