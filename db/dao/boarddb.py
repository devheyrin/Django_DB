from db.frame.sqlitedao import SqliteDao


class BoardDB(SqliteDao):
    def __init__(self, dbName):
        super().__init__(dbName);

    def insert(self, u):
        cc = self.getConn();