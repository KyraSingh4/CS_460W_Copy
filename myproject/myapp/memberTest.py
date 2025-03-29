from Member import President
from Directory import Directory
import psycopg2
from psycopg2 import sql
from Member import Member
import datetime

#p = President()

#p.createMember("test", "test", "test@test.com", "111-111-1113", True, 'test')

mem = Member(1)

print(mem.createReservation('singles', 0, datetime.time(10,00,00), datetime.time(11,15,00),7, [], ['Guesterino Test']))

tim = '10:15'

test = tim.split(":")
print(test)

print(datetime.time(int(test[0]),int(test[1])))