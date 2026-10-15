# Swat Perfumes / Rava Perfume

Ready-to-deploy Flask storefront with working `templates/index.html`.

## Render deployment
- Upload the **contents** of this folder to the root of your GitHub repository.
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
- Optional environment variables: `WHATSAPP_NUMBER` (country code + number, digits only, no plus sign), `STORE_BRAND`, `STORE_CURRENCY`, `SECRET_KEY`.
- Without `WHATSAPP_NUMBER`, ordering links are disabled instead of pointing to an incorrect number.
- `/health` returns JSON status.

## Local run
`pip install -r requirements.txt` then `python app.py`.

## Customize
Edit the `PRODUCTS` list in `app.py` for product names, descriptions and prices. Product bottle artwork is CSS-generated placeholder art, not real product photography. The bilingual toggle translates static interface text; product names and descriptions remain in English.
