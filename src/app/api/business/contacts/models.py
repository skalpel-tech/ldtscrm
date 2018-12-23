from flask_restplus import fields
from api.restplus import api

contact = api.model('Contact', {
"""
name and identifiers

"""
    'id': fields.String(readOnly=True, description='The unique identifier of a contact'),
    'suffix': fields.String(required=True, description='Suffix of a contact'),   
    'title': fields.String(required=True, description='Title of a contact'),  
    'last-name': fields.name(required=True, description='The last name of the contact'),
    'middle-names': fields.names(required=True, description='The middle name(s) of the contact'),
    'first-name': fields.name(required=True, description='The first name of the contact object'),
    'full-name': fields.name(required=True, description='The full name of the contact object'), 

"""
general data 

"""
    'description': fields.String(readOnly=True, description='Description of a contact'),
"""

address fields
https://en.wikipedia.org/wiki/ISO_3166-2

"""

    'city': fields.city(readOnly=True, description='City of contact address'),
    'country': fields.country(readOnly=True, description='Country of contact address'),
    'region': fields.region(readOnly=True, description='Region of contact address(e.g. State, Province, Territory, Region, District)'), //Please read: https://en.wikipedia.org/wiki/ISO_3166-2
    'street': fields.street(readOnly=True, description='Street of contact address'),
    'postal-code': fields.String(readOnly=True, description='Postal Code of contact address'),
    'latitude': fields.latitude(readOnly=True, description='Latitude of contact address'),
    'longitude': fields.longitude(readOnly=True, description='Longitude of contact address'),
    'alternate-address': fields.address(readOnly=True, description='Alternate address details of a contact, compound form'),
    'alternate-latitude': fields.latitude(readOnly=True, description='Alternate latitude of contact address'),
    'alternate-longitude': fields.longitude(readOnly=True, description='Alternate longitude of contact address'),

"""

phone number information

"""

 'phone-number': fields.Phone(readOnly=True, description='Phone Number of a contact, label should be business phone'),
 'home-phone': fields.Phone(readOnly=True, description='Phone Number of a contact'),
 'do-not-call': fields.Boolean(readOnly=True, description='Indicates that the contact does not want to receive calls.'),
 
 
"""

email information

"""

'email': fields.Email(readOnly=True, description='Email of contact address'),
'Opted-out-of-email': fields.Boolean(readOnly=True, description='Indicates whether the contact doesn’t want to receive email'),

"""

fax information

"""
'fax': fields.fax(readOnly=True, description='Fax number of contact.'),
'opted-out-of-fax': fields.Boolean(readOnly=True, description='Indicates whether the contact prohibits receiving faxes.'),


"""

activity information

"""
'last-activity-date': fields.date(readOnly=True, description='Last date where an event was logged for a contact.'),
'last-viewed-date': fields.date(readOnly=True, description='Last date where a contact was viewed.'),



})