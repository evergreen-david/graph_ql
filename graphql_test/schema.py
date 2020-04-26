from graphene import ObjectType, Schema

from user.graphql.schema import Query as InfoQuery
from user.graphql.schema import Mutation as InfoMutation

class Query(InfoQuery, ObjectType):
    pass

class Mutation(InfoMutation, ObjectType):
    pass

schema = Schema(query=Query,  mutation=Mutation)
