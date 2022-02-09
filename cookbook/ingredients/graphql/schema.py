import graphene

from cookbook.ingredients.graphql.types import CategoryType, IngredientType
from cookbook.ingredients.models import Category, Ingredient


class IngredientsQueries(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


# class IngredientsMutations(graphene.Mutation):
#     pass
