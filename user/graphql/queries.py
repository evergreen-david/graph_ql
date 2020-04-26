import graphene
from graphene_django.types import DjangoObjectType, ObjectType

from ..models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User

class Query(ObjectType):
    user = graphene.Field( UserType, id=graphene.Int() )
    users = graphene.List(UserType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()
