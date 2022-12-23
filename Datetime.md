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

### date.fromisoformat('YYYY-MM-DD')

(Python version 3.7)

Allows us to make a date obejct a string (format compliant with **ISO 8601** standard) argument.

Be sure to add 0 before a month or a day that is expressed by a number less than 10.

### ISO 8601

standard defines how the date and time are represented.

### Date and time operations

The **timedelta** in the datetime module that was created for just such a purpose.

To create a timedelta object, we neeed to perform subtraction on date or datetime objects.

```python
from datetime import date, datetime

d1 = date(2022,11,4)
d2 = date(2019, 11, 4)

print(d1 - d2)

```

## Event logging

from the datetime module we are able to determine when an error occurs. When creating logs, you can specify the date and time format;
