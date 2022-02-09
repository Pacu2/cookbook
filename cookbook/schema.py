import graphene

from .ingredients.graphql.schema import IngredientsQueries  # IngredientsMutations,

# class Mutations(
#     IngredientsMutations,
# ):
#     pass


class Queries(
    IngredientsQueries,
):
    pass


schema = graphene.Schema(
    query=Queries,
    # mutations=Mutations,
)
