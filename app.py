from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

# @app.route('/ping')
# def ping():
#     return jsonify({"message": "Pong!"})

@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "Product's List"})


@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if(len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"message": "Product not found"})



@app.route('/products/prices/<int:product_price_a>&<int:product_price_b>')
def getProductByPrice(product_price_a, product_price_b):
    productsFounds = [product for product in products if product['price'] != "AGOTADO" if (int(product['price']) >= product_price_a) and (int(product['price'] <= product_price_b))]
    
    # product for product in products:
    #     if product['price'] != "AGOTADO":
    #         if int(product['price'] > product_price_a):
    #             productsFounds = product['price']

    if(len(productsFounds) > 0):
        return jsonify({"product": productsFounds})
    return jsonify({"message": "Products by prices not found"})


@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "description": request.json['description'],
        "price": request.json['price'],
    }
    products.append(new_product)
    return jsonify(({"message": "Product Added Succesfully", "products": products}))



@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if(len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['description'] = request.json['description']
        productFound[0]['price'] = request.json['price']
        return jsonify({
            "message": "Product Updated",
            "product": productFound[0]
        })
    return jsonify({"message": "Product Not Found"})




@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            "message": "Product Deleted",
            "products": products
        })
    return jsonify({"message": "Product Not Found"})



if __name__ == '__main__':
    app.run(debug=True, port=4000)