# encoding: utf-8
"""
Contact database models
--------------------
"""
import uuid

from sqlalchemy_utils import Timestamp
from sqlalchemy.dialects.postgresql import UUID

from app.extensions import db

class Contact(db.Model, Timestamp):
    """
    Contact database model.
    """
    id = db.Column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        primary_key=True) # pylint: disable=invalid-name
    suffix = db.Column(
        db.String(length=80),
        default='',
        nullable=False)
    title = db.Column(
        db.String(length=80),
        default='',
        nullable=False)
    last_name = db.Column(
        db.String(),
        default='',
        nullable=False)
    middle_names = db.Column(
        db.String(),
        default='',
        nullable=False)
    first_name = db.Column(
        db.String(),
        default='',
        nullable=False)
    full_name = db.Column(
        db.String(),
        default='',
        nullable=False)
    description = db.Column(
        db.String(),
        default='',
        nullable=False)
    city = db.Column(
        db.String(),
        default='',
        nullable=False)
    country = db.Column(
        db.String(length=120),
        default='',
        nullable=False)
    region = db.Column(
        db.String(length=120),
        default='',
        nullable=False)
    street = db.Column(
        db.String(),
        default='',
        nullable=False)
    postal_code = db.Column(
        db.String(length=80),
        default='',
        nullable=False)

    def __init__(
        self, 
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
        postal_code):
        self.id = str(uuid.uuid4())
        self.suffix = suffix 
        self.title = title
        self.last_name = last_name
        self.middle_names = middle_names
        self.first_name = first_name
        self.full_name = "%s %s %s" % (first_name, middle_names, last_name)
        self.description = description
        self.city = city
        self.country = country
        self.region = region
        self.street = street
        self.postal_code = postal_code
