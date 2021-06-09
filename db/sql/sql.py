class Sql:
    make_userdb = ''' CREATE  TABLE  IF NOT EXISTS USERDB (
        ID  TEXT  PRIMARY KEY,
        PWD  TEXT,
        NAME TEXT
    ) ''';

    # 회원 CRUD
    insert_userdb = ''' INSERT  INTO  USERDB VALUES (?,?,?) ''';
    update_userdb = ''' UPDATE  USERDB  SET  PWD=?,  NAME=?  WHERE  ID=? ''';
    delete_userdb = ''' DELETE  FROM  USERDB  WHERE  ID=? ''';
    select_userdb = ''' SELECT  *  FROM  USERDB  WHERE ID=? ''';
    selectall_userdb = ''' SELECT  * FROM USERDB ''';

    make_itemdb = '''  
         CREATE  TABLE  IF  NOT  EXISTS  ITEMDB (
           ID INTEGER  PRIMARY KEY  AUTOINCREMENT,
           NAME  TEXT,
           PRICE  REAL,
           REGDATE  DATE  DEFAULT  (DATETIME('now', 'localtime'))
         ) 
     ''';

    make_boarddb = '''  
             CREATE  TABLE  IF  NOT  EXISTS  BOARDDB (
               ID INTEGER  PRIMARY KEY  AUTOINCREMENT,
               NAME  TEXT,
               TITLE  TEXT,
               CONTENT TEXT,
               REGDATE  DATE  DEFAULT  (DATETIME('now', 'localtime'))
             ) 
         ''';

    # 상품 CRUD
    insert_itemdb = '''  
         INSERT  INTO  ITEMDB (NAME,PRICE) VALUES  (?,?) 
     ''';
    update_itemdb = '''  
         UPDATE  ITEMDB  SET  NAME=?,  PRICE=?  WHERE ID=? 
     ''';
    delete_itemdb = '''  
         DELETE   FROM  ITEMDB  WHERE  ID = ? 
     ''';
    select_itemdb = '''   
         SELECT  *  FROM  ITEMDB  WHERE  ID = ?
     ''';
    selectall_itemdb = '''   
         SELECT  * FROM  ITEMDB
     ''';

    # 게시판 CRUD
    insert_boarddb = '''INSERT  INTO  BOARDDB (NAME,TITLE,CONTENT) VALUES  (?,?,?) ''';
    update_boarddb = '''  
         UPDATE  BOARDDB  SET  TITLE=?,  CONTENT=?  WHERE ID=? 
     ''';
    delete_boarddb = '''  
         DELETE   FROM  BOARDDB  WHERE  ID = ? 
     ''';
    select_boarddb = '''   
         SELECT  *  FROM  BOARDDB  WHERE  ID = ?
     ''';
    selectall_boarddb = '''   
         SELECT  * FROM  BOARDDB
     ''';