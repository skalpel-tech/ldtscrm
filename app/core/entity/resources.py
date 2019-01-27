# coding: utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
"""
    Entity Related HTTP resources
    ========================

    File contains HTTP resources for an Entity module
"""

from flask import request, abort
from sqlalchemy.exc import IntegrityError
from app.core.entity.models import EntityType
from app import blueprint
from app.extensions import db


def init_routes():
    bootstrap_entity_type_routes()
    # bootstrap_entity_routes()


def bootstrap_entity_type_routes():

    @blueprint.route('entity-type/<string:entity_id>', methods=['GET'])
    def get_entity_type_by_id(entity_id):
        entity_type = EntityType.query.get(entity_id)
        if not entity_type:
            abort(404, description='Entity Type not found')
        return entity_type.json()

    @blueprint.route('entity-type/<string:entity_id>', methods=['DELETE'])
    def delete_entity_type_by_id(entity_id):
        entity_type = EntityType.query.get(entity_id)
        if not entity_type:
            abort(404, description='Entity Type not found')

        db.session.begin()
        db.session.delete(entity_type)
        db.session.commit()

        return "Entity Type deleted", 200

    @blueprint.route('entity-type', methods=['POST'])
    def create_entity_type():
        if not request.json:
            abort(400, description='Content type not supported')

        entity_schema = request.get_json().get('schema')
        if not entity_schema:
            abort(400, description='Entity type "schema" not provided')

        entity_type_name = request.get_json().get('name')
        if not entity_type_name:
            abort(400, description='Entity type "name" not provided')

        entity_type: EntityType = EntityType(
            schema=entity_schema,
            name=entity_type_name
        )

        db.session.begin()
        db.session.add(entity_type)
        try:
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                description="Entity Type '{}' is not unique".format(entity_type.name)
            )

        return entity_type.json(), 201


# def bootstrap_entity_routes():

    # @blueprint.route('entity/<string:entity_id>', methods=['GET'])
    # def get_entity_by_id(entity_id):
    #     return jsonify(Entity.query.get(entity_id))
