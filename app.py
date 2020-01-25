from flask import Flask, request, redirect, url_for, render_template
from databases import get_all_recipes, delete_by_id, add_recipe

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route('/', methods=['GET' , 'POST'])
def homepage():
	if request.method == 'GET':
		return render_template("home.html")
	else:
		deleted = request.form['deleted']
		delete_by_id(deleted)
		return render_template("home.html")


@app.route('/uri', methods=['GET' , 'POST'])
def uri():
	return render_template("uri.html")


@app.route('/recipes', methods=['GET' , 'POST'])
def recipes():
	if request.method == 'GET':
		recipes = get_all_recipes()
		return render_template("recipes.html", recipes = recipes)
	else:
		creator = request.form['creator']
		syrop = request.form['syrop']
		topping = request.form['topping']
		add_recipe(creator, syrop, topping)
		recipes = get_all_recipes()
		return render_template("recipes.html", recipes = recipes)


@app.route('/admin', methods=['GET' , 'POST'])
def admin():
	if request.method == 'GET':
		recipes = get_all_recipes()
		return render_template("login.html", recipes = recipes)
	else:
		recipes = get_all_recipes()
		psw = request.form['psw']
		if psw == 'admin123':
			return render_template("admin.html", recipes = recipes)
		else:
			return render_template("login.html", recipes = recipes, wrongP = True)
		
# @app.route('/store')
# def store():
# 	products = get_all_products()
# 	return render_template("store.html", products = products)

# @app.route('/about')
# def about():
# 	return render_template("about.html")


# @app.route('/cart', methods=['GET' , 'POST'])
# def cart():
# 	if request.method == 'GET':
# 		userCart = get_cart()
# 		allProducts = get_all_products()
# 		return render_template("cart.html", allProducts = allProducts, userCart = userCart)
# 	else:
# 		added = request.form['added']
# 		add_to_cart(added)
# 		userCart = get_cart()
# 		allProducts = get_all_products()
# 		return render_template("cart.html", allProducts = allProducts, userCart = userCart)

if __name__ == '__main__':
    app.run(debug=True)

