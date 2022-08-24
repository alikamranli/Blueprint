from flask import render_template, request, redirect, url_for, flash,jsonify
from admin import admin_bp
from admin.forms import CustomerForm, ProductForm
@admin_bp.route('/')
def admin_index():
    return render_template('admin/index.html')

@admin_bp.route('/about')
def admin_about():
    return 'This is about page'

@admin_bp.route('/create',methods=['GET','POST'])
def admin_product_create():
    from models import Product
    from start import db
    productForm=ProductForm()
    if request.method=='POST':
        product=Product(
        brand=productForm.brand.data,
        model=productForm.model.data,
        description=productForm.description.data)
        db.session.add(product)
        db.session.commit()
        return redirect('/admin/list')
    return render_template('/admin/create.html',productForm=productForm)

@admin_bp.route('/customers',methods=['GET','POST'])
def admin_customers():
    customerForm=CustomerForm()
    from start import db
    from models import Customer
    return render_template('/admin/customer.html')

@admin_bp.route('/list',methods=['GET','POST'])
def products():
    from models import Product,db
    products=Product.query.all()
    return render_template('/admin/list.html',products=products)

@admin_bp.route('/delete/<id>',methods=['GET','POST'])
def delete(id):
    from models import Product
    from start import db
    pr=Product.query.get(id)
    db.session.delete(pr)
  
    db.session.commit()
    return redirect('/list')
@admin_bp.route('/update/<id>',methods=['GET','POST'])
def update(id):
    from models import Product
    from start import db
    prodct=Product.query.get(id)
    productForm=ProductForm()
    if request.method=='POST':
        product=Product(
        brand=productForm.brand.data,
        model=productForm.model.data,
        description=productForm.description.data)
        db.session.add(product)
        db.session.commit()
        return redirect('/admin/list')
    return render_template('/admin/create.html',productForm=productForm)
