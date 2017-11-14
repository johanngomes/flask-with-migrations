from flask import Flask 

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine('postgresql://jgomes:1234@localhost/flaskdb', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()

class Example(Base):
   __tablename__ = 'examples'

   id = Column(Integer, primary_key=True)
   name = Column(String)
   alternative_name = Column(String)

   def __init__(self, name=None):
   		self.name = name
   		self.alternative_name = alternative_name

   def __repr__(self):
      return "<Example(name='%s')>" % (self.name)

def add_new_example():
	first_example = Example('some-example')
	second_example = Example('some-other-example')
	
	db_session.add(first_example)
	db_session.add(second_example)

	db_session.commit()

def remove_added_example():
	example = db_session.query(Example).filter_by(name='some-example').first()
	db_session.delete(example)

	db_session.commit()

def edit_a_example():
	example = db_session.query(Example).filter_by(name='some-example').first()
	example.name = 'some-example-edited'

	db_session.commit()

@app.route('/')
def index():
	return 'hello flask'

@app.route('/add')
def add():
	add_new_example()	
	return 'added new examples'

@app.route('/delete')
def delete():
	remove_added_example()
	return 'removed first example'

@app.route('/edit')
def edit():
	edit_a_example()
	return 'edited first example'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
	app.run()
