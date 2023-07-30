from src.models.dish import Dish
from src.models.ingredient import Ingredient
import pytest


def test_dish():
    bacon = Ingredient("bacon")
    dish_name = "Macarrão"
    dish = Dish(dish_name, 29.99)

    assert dish.name == dish_name
    assert dish.recipe == {}

    dish.add_ingredient_dependency(bacon, 6)
    assert dish.recipe == {bacon: 6}
    assert dish.get_ingredients() == {bacon}

    assert dish.__eq__(dish) is True

    assert dish.__hash__() == hash("Dish('Macarrão', R$29.99)")

    assert dish.get_restrictions() == bacon.restrictions

    with pytest.raises(TypeError):
        Dish("Macarrão", "20.0")

    with pytest.raises(ValueError):
        Dish("Macarrão", -1.0)
