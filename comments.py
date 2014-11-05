#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

import datetime


comments = [
{
  "parent":"Post 49",
  "username":"SomeUser5098",
  "contents":'''I GOT STUFF TO SAY''',
  "id":"hackid1",
  "date_posted":datetime.date(2014, 11, 5)
},

{
  "parent":"hackid1",
  "username":"AnotherUser5098",
  "contents":'''I GOT STUFF TO SAY''',
  "id":"hackid2",
  "date_posted":datetime.date(2014, 11, 6)
},
{
  "parent":"hackid1",
  "username":"AnotherUser5098",
  "contents":'''I GOT STUFF TO SAY''',
  "id":"hackid3",
  "date_posted":datetime.date(2014, 11, 6)
},
{
  "parent":"Post 49",
  "username":"SomeUser5098",
  "contents":'''I no longer have stuff to say.<br/><br/>Thank you for your time.''',
  "id":"hackid15",
  "date_posted":datetime.date(2014, 11, 5)
},


]
