# coding: utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :

"""
    Entity Related DB models
    ========================

    File contains DB models for an Entity module

     - EntityType
     - Entity
     - EntityAudit
"""

import uuid, json

from app.extensions import db
from sqlalchemy_utils import Timestamp


class EntityType(db.Model, Timestamp):
    """ **EntityType** db model """

    __tablename__ = 'entity_type'

    id = db.Column(
        db.String(length=60),
        unique=True,
        nullable=False,
        primary_key=True
    )

    name = db.Column(
        db.String(length=80),
        unique=True,
        nullable=False,
        default=''
    )

    schema = db.Column(
        db.Text(),
        nullable=False
    )

    def __init__(self, **kwargs):
        self.id = uuid.uuid4().__str__()
        self.name = kwargs.get('name')
        self.schema = kwargs.get('schema')

    def json(self):
        data = dict([])
        data['id'] = self.id
        data['name'] = self.name
        data['schema'] = self.schema
        return json.dumps(data)


class Entity(db.Model, Timestamp):
    """ **Entity** db model """

    __tablename__ = 'entity'

    id = db.Column(
        db.String(length=60),
        unique=True,
        nullable=False,
        primary_key=True,
        default=uuid.uuid4().__str__
    )

    entityTypeId = db.Column(
        db.String(length=60),
        db.ForeignKey('entity_type.id'),
        nullable=False
    )

    content = db.Column(
        db.Text(),
        nullable=False
    )


class EntityAudit(db.Model, Timestamp):
    """ **Entity Audit** db model """

    __tablename__ = 'entity_audit'

    id = db.Column(
        db.String(length=60),
        unique=True,
        nullable=False,
        primary_key=True,
        default=uuid.uuid4().__str__
    )

    updatedEntityId = db.Column(
        db.String(length=60),
        db.ForeignKey('entity.id'),
        nullable=False
    )

    action = db.Column(
        db.String(length=20),
        nullable=False
    )

    originalEntityContent = db.Column(
        db.Text(),
        nullable=False
    )

    changedByEntityId = db.Column(
        db.String(length=60),
        db.ForeignKey('entity.id'),
        nullable=False
    )
