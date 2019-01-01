# encoding: utf-8
"""
User database models
--------------------
"""
import enum

from sqlalchemy_utils import types as column_types, Timestamp

from app.extensions import db

class Contact(db.Model, Timestamp):
    """
    User database model.
    """

    id = db.Column(db.Integer, primary_key=True) # pylint: disable=invalid-name
    suffix = db.Column(
        db.String(length=30), 
        default='', 
        nullable=False)
    title = db.Column(
        db.String(length=120), 
        default='', 
        nullable=False)
    last_name = db.Column(
        db.String(length=30), 
        default='', 
        nullable=False)
    middle_names  = db.Column(
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
        db.String(120), 
        default='', 
        nullable=False)
    region = db.Column(
        db.String(120), 
        default='', 
        nullable=False)
    street = db.Column(
        db.String(), 
        default='', 
        nullable=False)
    postal_code = db.Column(
        db.String(30), 
        default='', 
        nullable=False)
    alternate_address = db.Column(
        db.String(), 
        default='', 
        nullable=False)
