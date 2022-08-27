from flask import render_template, request, redirect, url_for, flash,jsonify
from admin import admin_bp
from admin.forms import CustomerForm, ProductForm


@admin_bp.route('/')
def admin_index():
    return render_template('admin/index.html')



@admin_bp.route('/products')
def admin_products():
    from start import db
    from models import Product
    products=Product.query.all()
    productForm=ProductForm
    return render_template('admin/products.html',productForm=productForm,products=products)
