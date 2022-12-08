# DateTime

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

### Unix epoch

This is when the counting of time began on Unix systems.
To create a date from a timestamp, we must pass a Unix timestamp to **fromtimestamp** method.
**time()** returns the number of seconds from January 1, 1970 to the current moment in the form of a float number. 
In Unix and Windows systems, leap seconds aren't counted.

A different way to show when mother threw a zapato at you.

```python

from datetime import date
import time

impact_timestamp = time.time()
print("Timestamp: ", impact_timestamp)

d = date.fromtimestamp(impact_timestamp)

print("Date:", d)

```
