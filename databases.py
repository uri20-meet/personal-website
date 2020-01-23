from model import Base, Recipe

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_recipe(creator, syrop, topping):
	recipe = Recipe(
		creator = creator, 
		syrop = syrop, 
		topping = topping)
	session.add(recipe)
	session.commit()

def delete_by_id(recipeId):
	session.query(Recipe).filter_by(recipeId = recipeId).delete()
	session.commit()

def get_all_recipes():
	return(session.query(Recipe).all())

def get_by_id(id):
	return(session.query(Recipe).filter_by(id = id))

def get_by_name(creator):
	return(session.query(Recipe).filter_by(creator = creator))