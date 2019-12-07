# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import QuantLib as ql
date1 = ql.Date(1, 1, 2015)
date2 = ql.Date(1, 1, 2016)
tenor = ql.Period(ql.Monthly)
calendar = ql.UnitedStates()
schedule = ql.Schedule(date1, date2, tenor, calendar, ql.Following, ql.Following, ql.DateGeneration.Forward, False)
list(schedule)
#%%
print(date1)
print(list(schedule))