import pandas as pd

red_df = pd.read_csv("C:\Temp\python\DataAnalyze\week13\winequality-red.csv", sep=';', header=0)
white_df = pd.read_csv("C:\Temp\python\DataAnalyze\week13\winequality-white.csv", sep=';', header=0)
red_df.to_csv('wine_red.csv', index=False)
white_df.to_csv('wine_white.csv', index=False)


#quality는 종속변수