from .db_connection_handler import DBConnectionHandler

def test_db_connection_handler():
  db_conn_handler=DBConnectionHandler()

  assert db_conn_handler.session is None