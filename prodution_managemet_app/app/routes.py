from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
from app import app
from app.models import User
from app.models import Inventory, Order, Quality, Schedule


@app.route('/')
def home():
    return render_template('base.html')

@app.route('/dashboard')
@login_required
def dashboard():
    # Retrieve necessary data for the dashboard
    orders = Order.query.all()
    inventory = Inventory.query.all()
    schedules = Schedule.query.all()
    quality_records = Quality.query.all()

    # Render the dashboard template with the retrieved data
    return render_template('dashboard.html', orders=orders, inventory=inventory, schedules=schedules, quality_records=quality_records)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))
