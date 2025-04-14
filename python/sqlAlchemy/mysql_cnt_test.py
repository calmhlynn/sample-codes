import sqlalchemy as db

info = {
    "id": "root",
    "password": "password",
    "host": "localhost",
    "port": 3306,
}

# sql_db_url = f"mysql://{info['id']}:{info['password']}@{info['host']}/"

engine = db.create_engine(f"mysql://{info['id']}:{info['password']}@{info['host']}/")
connection = engine.connect()
metadata = db.MetaData()
table = db.Table('member', metadata, autoload=True, autoload_with=engine)


print(table.columns.keys())

