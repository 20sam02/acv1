from sqlalchemy import create_engine, MetaData


engine = create_engine("mysql+pymysql://s4m:s4mcrud12@localhost:3307/crudb")

meta = MetaData()

conn = engine.connect()