from pprint import pprint
import calendar
import math

hhh= dict(aa=54, bb=67, cc=6767, dd='hjhjh')

pprint(locals())
pprint(hhh)
c = calendar.TextCalendar() # firstweekday=0 - Monday, 6 - Sunday
print(c.formatyear(2024))
print(c.formatmonth(2024,3))
print(c.formatmonthname(2024, 4, 8))
pprint(dir(math))

