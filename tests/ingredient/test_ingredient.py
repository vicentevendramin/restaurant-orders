from src.models.ingredient import Ingredient, Restriction, restriction_map


# Req 1
def test_ingredient():
    # Restrictions
    ingredient_name = "salmão"
    ingredient = Ingredient(ingredient_name)
    assert isinstance(ingredient, Ingredient)
    assert ingredient.name == ingredient_name

    ingredient_restrictions = restriction_map().get(ingredient_name, set())
    assert ingredient.restrictions == ingredient_restrictions

    # __repr__
    ingredient_repr = ingredient.__repr__()
    assert ingredient_repr == f"Ingredient('{ingredient_name}')"
    assert ingredient_repr == repr(ingredient)
    assert ingredient_repr != repr(Ingredient("manteiga"))

    # __eq__
    ingredient_eq = ingredient.__eq__(ingredient)
    assert ingredient_eq

    # __hash__
    ingredient_hash = ingredient.__hash__()
    assert ingredient_hash == hash(ingredient_name)

    ingredient_any_name = "manteiga"
    ingredient_any = Ingredient(ingredient_any_name)
    assert ingredient_any.name == ingredient_any_name
    assert ingredient_hash != hash(ingredient_any)

    ingredient_restrictions = {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
    assert ingredient_any.restrictions == ingredient_restrictions

    # -- -- --
    assert not ingredient.__eq__(ingredient_any)

    ingredient_any_repr = Ingredient(ingredient_any_name).__repr__()
    assert ingredient_any_repr == f"Ingredient('{ingredient_any_name}')"
    assert ingredient_any_repr == repr(ingredient_any)
    assert ingredient_any_repr != repr(ingredient)

    ingredient_any_hash = Ingredient(ingredient_any_name).__hash__()
    assert ingredient_any_hash == hash(ingredient_any_name)

    assert ingredient_hash != ingredient_any_hash

    ingredient_x_name = "ovo"
    ingredient_x = Ingredient(ingredient_x_name)
    ingredient_x_repr = f"Ingredient ('{ingredient_x_name}')"
    assert ingredient_x_repr == repr(ingredient_x)
    assert ingredient_x_repr != repr(ingredient_any)
    assert ingredient_x_repr != repr(ingredient)
