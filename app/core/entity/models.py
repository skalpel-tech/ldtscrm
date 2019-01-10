'''
    File contains DB models for a Entity models
'''
import uuid

from app.extensions import db
from sqlalchemy_utils import Timestamp


class EntityType(db.Model, Timestamp):
    __tablename__ = 'entity_type'

    id = db.Column(
        db.String(length=60),
        unique=True,
        nullable=False,
        primary_key=True,
        default=uuid.uuid4().__str__
    )

    schema = db.Column(
        db.Text(),
        nullable=False
    )

class Entity(db.Model, Timestamp):

    __tablename__ = 'entity'

    id = db.Column(
        db.String(length=60),
        unique=True,
        nullable=False,
        primary_key=True,
        default=uuid.uuid4().__str__
    )

    entityId = db.Column(
        db.String(length=60),
        db.ForeignKey('entity_type.id'),
        nullable=False
    )

    hrId = db.Column(
        db.String(length=60),
        db.ForeignKey('entity.id'),
        nullable=False
    )

    content = db.Column(
        db.Text(),
        nullable=False
    )


class EntityAudit(db.Model):

    __tablename__ = 'entity_audit'

    id = db.Column(
        db.String(length=60),
        unique=True,
        nullable=False,
        primary_key=True,
        default=uuid.uuid4().__str__
    )

    changedEntityId = db.Column(
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
