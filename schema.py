import graphene

import users.schema
import gear.schema


class Query(users.schema.Query, gear.schema, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
