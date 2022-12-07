# datetime

## date

objects of this class represent a date (year,month,and day).

Below is a possible snippet of a program that possibly could be used to record the dates you upset your mom and see a zapato flying in your direction.

```python
# ZAPATO IMPACT
from datetime import date

date_of_impact = date.today()

statementA = "zapato impact: "

print(statementA , date_of_impact, sep = " ")

```

The above code uses the 'today' method and returns a date object. The date object has three attributes: 'year,month, and day'. These three attributes are read only.

### Restrictions

year parameter (y):
    MINYEAR = 1 $ \leq y \leq $ 9999 = MAXYEAR

month parameter (m):
    $1 \leq m \leq 12 $

day parameter (d):
    $ 1 \leq d \leq $ (last day of month)
