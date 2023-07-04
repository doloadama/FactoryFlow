from flask import render_template, request, redirect, url_for
from app import app
from app.models import Order, Inventory, Schedule, Quality, Report


@app.route('/')
def dashboard():
    # Retrieve necessary data for the dashboard
    # Example:
    orders = Order.query.all()
    inventory = Inventory.query.all()
    schedules = Schedule.query.all()
    quality_records = Quality.query.all()
    
    # Render the dashboard template with the retrieved data
    return render_template('dashboard.html', orders=orders, inventory=inventory, schedules=schedules, quality_records=quality_records)
