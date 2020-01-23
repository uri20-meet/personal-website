from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Recipe(Base):
	"""docstring for ClassName"""
	__tablename__ = 'recipes'
	recipeId = Column(Integer, primary_key = True)
	creator = Column(String)
	syrop = Column(String)
	topping = Column(String)
	
	def __repr__(self):
		return("recipeId: {} \n"
			"creator: {} \n"
			"syrop: {} \n"
			"topping: {} \n"
			).format(self.recipeId,
			self.creator,
			self.syrop,
			self.topping)