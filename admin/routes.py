
from flask import render_template, request, redirect, url_for, flash,jsonify
from admin import admin_bp
from admin.forms import CustomerForm, ProductForm


@admin_bp.route('/')
def admin_index():
    return render_template('admin/index.html')



@admin_bp.route('/products', methods=['GET','POST'])
def admin_products():
    from start import db
    from models import Product
    products=Product.query.all()
    productForm=ProductForm()

    if request.method=="POST":
        brand=productForm.brand.data
        model=productForm.model.data
        description=productForm.description.data
        product=Product(brand,model,description)
        db.session.add(product)
        db.session.commit()
        return redirect('/admin/products')  
    return render_template('admin/products.html',productForm=productForm,products=products)
