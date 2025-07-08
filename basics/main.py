from sqlalchemy import create_engine, text  

engine = create_engine('sqlite:///./basics/database.db', echo=True)

conn = engine.connect()

conn.execute(text("CREATE TABLE IF NOT EXISTS people (name str, age int)"))

conn.commit()



from sqlalchemy.orm import Session

Session = Session(engine)

Session.execute(text("INSERT INTO people (name, age) VALUES ('nova', 999)"))

Session.commit()