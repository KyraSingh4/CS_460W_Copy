from Member import President
from Directory import Directory
import psycopg2
from psycopg2 import sql
from Member import Member
from datetime import timedelta, datetime
from datetime import time as dt
from Directory import Directory
from Calendar import Calendar
from emailer import Emailer

#p = President()

#p.createMember("test", "test", "test@test.com", "111-111-1113", True, 'test')

#mem = Member(5)

#print(mem.createReservation('singles', 0, datetime.time(10,0), datetime.time(11,00),10, [], ['Guesterino Test']))

#mem.updateReservation(32, ['Gavin VanNest'])

#print(dir.nameLookup('Ryder', 'Gover'))

start = dt(11,00,00)
end = dt(12,00,00)
print(datetime.combine(datetime.today(),end)-datetime.combine(datetime.today(),start) <= timedelta(minutes=60))