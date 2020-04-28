import graphene
from graphene_django.types import DjangoObjectType, ObjectType

from ..models import Menu

class MenuType(DjangoObjectType):
    class Meta:
        model = Menu

class Query(ObjectType):
    menu = graphene.Field( MenuType, id=graphene.Int() )
    menus = graphene.List(MenuType)

    def resolve_menus(self, info, **kwargs):
        return Menu.objects.all()
