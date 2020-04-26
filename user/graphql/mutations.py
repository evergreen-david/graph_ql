import graphene

from .queries import UserType
from ..models import User

class UserInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()

class CreateUser(graphene.Mutation):
    class Arguments:
        input = UserInput(required=True)

    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, input=None):
        user_instance = User(name=input.name)
        user_instance.save()
        return CreateUser(user=user_instance)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
