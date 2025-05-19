# kuzu-serial-string-pk

uv run main.py
Traceback (most recent call last):
  File "/Users/bgoosman/kineviz/kuzu/string-and-serial/main.py", line 23, in <module>
    result = conn.execute("MATCH (n) RETURN count(n)")
  File "/Users/bgoosman/.cache/uv/environments-v2/main-197a8a4bca35307d/lib/python3.13/site-packages/kuzu/connection.py", line 130, in execute
    _query_result = self._connection.query(query)
RuntimeError: Binder exception: Expected the same data type for property id but found STRING and SERIAL.