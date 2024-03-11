import pandas as pd
import numpy as np

div_line = '-' * 120

df = pd.DataFrame({
    'name': ['Jane', 'John', 'Ashley', 'Mike', 'Emily', 'Jack', 'Catlin'],
    'ctg': ['A', 'A', 'C', 'B', 'B', 'C', 'B'],
    'val': np.random.random(7).round(2),
    'val2': np.random.randint(1, 10, size=7)
})

def dprint(*args):
    print(*args, div_line, sep='\n')

if __name__ == '__main__':

    dprint('df', df)

    # 1. Логические Операторы
    df_04a = df[df.val > 0.4]
    df_04b = df[df['val'] > 0.4]
    dprint('df.val > 0.4', df_04a)
    dprint("df['val'] > 0.4", df_04a)

    # 2. Несколько Логических Операторов
    df_and = df[(df.val > 0.4) & (df.val2 > 3)] # and
    df_or = df[(df.val > 0.4) | (df.val2 > 3)] # or
    dprint('(df.val > 0.4) & (df.val2 > 3)', df_and)
    dprint('(df.val > 0.4) | (df.val2 > 3)', df_or)

    # 3. ISIN Метод
    names = ['John','Catlin','Mike']
    df_isin = df[df.name.isin(names)]
    dprint('df.name.isin(names)', df_isin)

    # 4. STR Аксессуар
    df_startswith = df[df.name.str.startswith('J')]
    df_contains = df[df.name.str.contains('y')]
    dprint("df.name.str.startswith('J')'", df_startswith)
    dprint("df.name.str.contains('y')", df_contains)

    # 5. ~ Тильда Означает отрицание НЕ
    df_tilda_start = df[~df.name.str.startswith('J')]
    dprint("~df.name.str.startswith('J')", df_tilda_start)

    # 6. QUERY (Запрос)
    query_text = "ctg == 'B' and val > 0.4"
    df_q = df.query(query_text)
    dprint("df.query(query_text)", df_q)

    # 7. nlargest, nsmallest Наибольшие, Наименьшие
    df_lardest = df.nlargest(3, 'val')
    df_smallest = df.nsmallest(2, 'val2')
    dprint("df.nlargest(3, 'val')", df_lardest)
    dprint("df.nsmallest(2, 'val2')", df_smallest)

    # - ``first``: prioritize the first occurrence(s)
    # - ``last``: prioritize the last occurrence(s)
    # - ``all``: keep all the ties of the smallest item even if it means
    df_sm_first = df.nsmallest(2, 'val2', 'first')
    df_sm_last = df.nsmallest(2, 'val2', 'last')
    df_sm_all = df.nsmallest(2, 'val2', 'all') # полезно если равных значений больше чем N
    dprint("nsmallest(2, 'val2', 'first')", df_sm_first)
    dprint("nsmallest(2, 'val2', 'last')", df_sm_last)
    dprint("nsmallest(2, 'val2', 'all')", df_sm_all)

    # 8. Loc и iloc
    # loc - метки строк (часто совпадают и индексами)
    # iloc - индексы строк.

    df_iloc = df.iloc[3:5, :] # 3, 4, 5 индексы строк, все столбцы
    df_loc = df.loc[3:5, :] # 3, 4, 5 метки строк, все столбцы
    dprint("По Индексам Строк", "iloc[3:5, :]", df_iloc)
    dprint("По Меткам Строк", "loc[3:5, :]", df_loc)

    indexes = ['a','b','c','d','e','f','g']
    print('Чтобы понять разницу. Поменяем метки на буквенные:', indexes)
    df.index = indexes
    df_loc = df.loc['b':'d', :]  # b, c, d метки строк, все столбцы
    dprint("По Меткам Строк", "loc['b':'d', :]", df_loc)

    df_loc_col = df.loc['b':'d', ['name', 'val']]
    dprint("df.loc['b':'d', ['name', 'val']]", df_loc_col)
