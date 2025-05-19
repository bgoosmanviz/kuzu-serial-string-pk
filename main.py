# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "kuzu",
#     "rich",
# ]
# ///

import kuzu
import shutil

path = "test"
if path:
    shutil.rmtree(path, ignore_errors=True)

db = kuzu.Database("test")
conn = kuzu.Connection(db)

conn.execute("CREATE NODE TABLE serial_pk (id SERIAL PRIMARY KEY, name STRING)")
conn.execute("CREATE NODE TABLE string_pk (id STRING PRIMARY KEY, name STRING)")
conn.execute("CREATE (n:serial_pk {name: 'John'})")
conn.execute("CREATE (n:string_pk {id: 'Alice', name: 'Alice'})")
result = conn.execute("MATCH (n) RETURN count(n)")

