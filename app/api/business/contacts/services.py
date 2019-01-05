# encoding: utf-8
"""
Contact Services
--------------------
"""

from app.extensions import db
from .models import Contact

def create_contact(data):
    suffix = data.get('suffix')
    title = data.get('title')
    last_name = data.get('last_name')
    middle_names = data.get('middle_names')
    first_name = data.get('first_name')
    description = data.get('description')
    city = data.get('city')
    country = data.get('country')
    region = data.get('region')
    street = data.get('street')
    postal_code = data.get('postal_code')
    new_contact = Contact(
        suffix,
        title,
        last_name,
        middle_names,
        first_name,
        description,
        city,
        country,
        region,
        street,
        postal_code)
    with db.session.begin():
        db.session.add(new_contact)
    return new_contact

def get_contact_by_id(contact_id):
    return Contact.query.get(contact_id)
