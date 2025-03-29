from Member import President
from Directory import Directory
import psycopg2
from psycopg2 import sql
from Calendar import Calendar

#p = President()

#p.createMember("test", "test", "test@test.com", "111-111-1113", True, 'test')

cal = Calendar()
print(cal.RetrieveDay(0))