# Design

## Main concept

This application will contain REST API backend only.
All external tools and UI will be introduced in an external repos

### Entities module
Implements features

 * Contact
 * Lead
 * Opportunity
 * Account

Graph model to be used to store information about contacts/leads. Where node will be called Entity and relation would still use the same name

Each entity would belong to one of EntityTypes that is a schema for entity validation. Some default entity types should be created. 

#### Proposed data structure

    EntityType:

        * id - entity type id
        * schema - JSON schema to be used for entity metadata validation

    Entity: 

        * id - some machine uuid
        * typeId - entity type used for validation
        * name - human readable entity id
        * content - JSON representing content

    EntityAudit:

        * entityId
        * action - CRUD
        * originalMeta

    RelationType:

        * id - Relation type id
        * fromEntity? - An entityType that can have that relation. Can be empty for all? Can be array? Should be part of schema?
        * toEntity? -  An entityType that can have that relation. Can be empty for all? Can be array? Should be part of schema?
        * schema - JSON schema to be used for Relation metadata validation

    Relation: 

        * id - some machine uuid
        * typeId - Relation type used for validation
        * fromEntity - entityLinked with relationship
        * toEntity - entityLinked with relationship
        * name - human readable Relation id
        * content - JSON representing content

    RelationAudit:

        * RelationId
        * action - CRUD
        * originalMeta

## Code structire