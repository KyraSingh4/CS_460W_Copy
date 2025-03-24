from Member import President
import psycopg2
from psycopg2 import sql

p = President()

p.createMember("test", "test", "test@test.com", "111-111-1113", True, 'test')