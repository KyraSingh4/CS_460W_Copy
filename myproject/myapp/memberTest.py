from Member import President
from Directory import Directory
import psycopg2
from psycopg2 import sql
from Member import Member
import datetime
from Directory import Directory
from Calendar import Calendar
#p = President()

#p.createMember("test", "test", "test@test.com", "111-111-1113", True, 'test')

mem = Member(1)

#print(mem.createReservation('singles', 0, datetime.time(10,0), datetime.time(11,00),10, [], ['Guesterino Test']))

#dir = Directory()

#print(dir.nameLookup('Ryder', 'Gover'))

mem.deleteReservation(22)