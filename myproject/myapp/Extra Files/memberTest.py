
from psycopg2 import sql
from ..Member import Member
from datetime import timedelta, datetime
from datetime import time as dt

m = Member(1)

print(m.getInformation())