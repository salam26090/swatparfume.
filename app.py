import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'change-this-in-production')
BRAND = os.environ.get('STORE_BRAND', 'Rava Perfume')
WHATSAPP = ''.join(c for c in os.environ.get('WHATSAPP_NUMBER', '') if c.isdigit())
CURRENCY = os.environ.get('STORE_CURRENCY', 'PKR')

PRODUCTS = [
    {'id': 1, 'name': 'Rava Oud', 'category': 'Oud', 'size': '100 ml', 'price': 2500, 'notes': 'Warm oud · Amber · Musk', 'color': 'oud'},
    {'id': 2, 'name': 'Rava Royal', 'category': 'Luxury', 'size': '100 ml', 'price': 2800, 'notes': 'Saffron · Rose · Woods', 'color': 'royal'},
    {'id': 3, 'name': 'Rava Blue', 'category': 'Fresh', 'size': '100 ml', 'price': 2400, 'notes': 'Citrus · Marine · Cedar', 'color': 'blue'},
    {'id': 4, 'name': 'Rava Bloom', 'category': 'Floral', 'size': '50 ml', 'price': 1600, 'notes': 'Jasmine · Vanilla · White musk', 'color': 'bloom'},
    {'id': 5, 'name': 'Rava Night', 'category': 'Luxury', 'size': '100 ml', 'price': 2900, 'notes': 'Spice · Leather · Tonka', 'color': 'night'},
    {'id': 6, 'name': 'Rava Musk', 'category': 'Musk', 'size': '50 ml', 'price': 1500, 'notes': 'Clean musk · Powder · Amber', 'color': 'musk'},
]

@app.route('/')
def home():
    category = request.args.get('category', 'All')
    products = [p for p in PRODUCTS if category == 'All' or p['category'] == category]
    categories = ['All'] + sorted({p['category'] for p in PRODUCTS})
    return render_template('index.html', products=products, categories=categories,
                           selected=category, brand=BRAND, whatsapp=WHATSAPP, currency=CURRENCY)

@app.route('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
