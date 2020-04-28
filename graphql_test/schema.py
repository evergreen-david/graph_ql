from graphene import ObjectType, Schema

from user.graphql.schema import Query as InfoQuery
from user.graphql.schema import Mutation as InfoMutation

from drink.graphql.schema import Query as DrinkQuery
# from drink.graphql.schema import Mutation as DrinkMutation


class Query(InfoQuery, DrinkQuery, ObjectType):
    pass

class Mutation(InfoMutation, ObjectType):
    pass

schema = Schema(query=Query,  mutation=Mutation)
