# encoding: utf-8
# pylint: disable=invalid-name,missing-docstring
"""
TEST suite for entity schemas
=============================
"""

from flask_restplus import marshal
from app.core.entity.schemas import entity_type

def test_entity_type_schema_empty():
    data = {'id': 'test', 'schema': {'key': 'test'}}
    dumped_result = marshal(data, entity_type)
    assert set(dumped_result.keys()) == {
        'name',
        'schema',
    }
    assert dumped_result['name'] == 'test'
