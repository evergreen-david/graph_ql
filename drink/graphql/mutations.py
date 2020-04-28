import graphene

from .queries import MenuType
from ..models import Menu

class MenuInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()

class CreateMenu(graphene.Mutation):
    class Arguments:
        input = MenuInput(required=True)

    menu = graphene.Field(MenuType)

    @staticmethod
    def mutate(root, info, input=None):
        menu_instance = Menu(name=input.name)
        menu_instance.save()
        return CreateMenu(user=menu_instance)

class Mutation(graphene.ObjectType):
    create_menu = CreateMenu.Field()
