from llama_index.core.tools.tool_spec.base import BaseToolSpec
from llama_index.tools.passio_nutrition_ai import NutritionAIToolSpec


def test_class():
    names_of_base_classes = [b.__name__ for b in NutritionAIToolSpec.__mro__]
    assert BaseToolSpec.__name__ in names_of_base_classes
