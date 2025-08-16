from pygments.lexers import sql
from sqlalchemy import create_engine, inspect, text
from wsproto import connection

db_connection_string = "postgresql://postgres:8888@localhost:5433/Lesson_9"
db = create_engine(db_connection_string)

#Получение информации о таблицах
def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[1] == 'subject'


def test_select():
    connections = db.connect()
    result = connections.execute(text("SELECT * FROM group_student"))
    rows = result.mappings().all()
    assert rows[0] == {'user_id': 42568, 'group_id': 184}


def test_insert():
    db = create_engine(db_connection_string).connect()
    sql = text("insert into subject(\"subject_id\", \"subject_title\") values (:new_id, :new_title)")
    rows = db.execute(sql, {'new_id': 888, 'new_title': 'Russian'})
    db.commit()


def test_update():
    db = create_engine(db_connection_string).connect()
    sql = text("UPDATE subject SET subject_title = :title WHERE subject_id = :id")
    rows = db.execute(sql, {'title': 'Amshen', "id": 888})
    db.commit()


def test_delete():
    db = create_engine(db_connection_string).connect()
    sql = text("DELETE From subject WHERE subject_id = :id")
    rows = db.execute(sql, {'id': 888})
    db.commit()


connection.close()