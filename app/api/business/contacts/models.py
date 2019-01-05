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

    # pylint: disable=too-many-instance-attributes
    # 13 is reasonable in this model.

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

    def __init__(self, **kwargs):
        valid_keys = [
            "suffix",
            "title",
            "last_name",
            "middle_names",
            "first_name",
            "description",
            "landline",
            "city",
            "country",
            "region",
            "street",
            "postal_code"]
        self.id = str(uuid.uuid4())
        for key in valid_keys:
            self.__dict__[key] = kwargs.get(key)
        self.full_name = "%s %s %s" % (self.first_name, self.middle_names, self.last_name)
