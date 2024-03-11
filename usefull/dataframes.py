import pandas as pd

column_names = ('ATOM', 'BTC', 'ETH')
indexes = ['free', 'used', 'total']
df = pd.DataFrame(columns=column_names, index=indexes)

if __name__ == '__main__':

    # print(df.columns)
    # if column_names[1] in df.columns:
    #     print(True)
    # else:
    #     print(False)

    # for i in indexes:
    #     df.loc[len(df)] = (10, 20, 30)

    df.loc['free'] = (99, 199, 299) # строка по метке
    df.loc['used'] = (1, 2, 3)
    df.loc['total'] = (100, 200, 300)

    print(df)
    value = df[column_names[0]][indexes[0]]
    print(value, type(value))