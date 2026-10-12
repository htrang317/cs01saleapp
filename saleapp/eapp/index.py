from itertools import product

from flask import Flask, render_template
from unicodedata import category

app=Flask(__name__)

@app.route('/')

def index():
    categories=[{
        'id':1,
        'name':'mobie'

    },{
        'id':2,
        'name':'tablet'
    },
        {
            'id': 3,
            'name': 'laptop'

        }    ]

    products=[{
        "id": 1,
        "name": "iPhone 7 Plus",
        "description": "Apple, 32GB, RAM: 3GB, iOS13",
        "price": 17000000,
        "image":"https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg","category_id": 1
    }, {
        "id": 2,
        "name": "iPad Pro 2020",
        "description": "Apple, 128GB, RAM: 6GB",
        "price": 37000000,
        "image":"https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg","category_id": 2
    }, {
        "id": 3,
        "name": "Galaxy Note 10 Plus",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg","category_id": 1
    },{
        "id": 1,
        "name": "iPhone 7 Plus",
        "description": "Apple, 32GB, RAM: 3GB, iOS13",
        "price": 17000000,
        "image":"https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg","category_id": 1
    }, {
        "id": 2,
        "name": "iPad Pro 2020",
        "description": "Apple, 128GB, RAM: 6GB",
        "price": 37000000,
        "image":"https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg","category_id": 2
    }, {
        "id": 3,
        "name": "Galaxy Note 10 Plus",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg","category_id": 1
    },{
        "id": 1,
        "name": "iPhone 7 Plus",
        "description": "Apple, 32GB, RAM: 3GB, iOS13",
        "price": 17000000,
        "image":"https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg","category_id": 1
    }, {
        "id": 2,
        "name": "iPad Pro 2020",
        "description": "Apple, 128GB, RAM: 6GB",
        "price": 37000000,
        "image":"https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg","category_id": 2
    }, {
        "id": 3,
        "name": "Galaxy Note 10 Plus",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg","category_id": 1
    }]

    return render_template('index.html', categories=categories, products=products)

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)

