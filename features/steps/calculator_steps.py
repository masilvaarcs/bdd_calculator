"""
Este módulo contém as etapas de teste BDD para a funcionalidade da calculadora.
"""

from behave import given, when, then
from calculator import soma


# Etapa: Dado que um número foi inserido na calculadora
@given("I have entered {num:d} into the calculator")
def step_impl(context, num):
    """
    Etapa que define que um número foi inserido na calculadora.

    Args:
        context: O objeto de contexto do Behave.
        num: O número a ser inserido na calculadora.
    """
    if not hasattr(context, "numbers"):
        context.numbers = []
    context.numbers.append(num)


# Etapa: Quando eu pressionar o botão de adição
@when("I press the add button")
def step_impl(context):
    """
    Etapa que define a ação de pressionar o botão de adição.

    Args:
        context: O objeto de contexto do Behave.
    """
    context.result = soma(*context.numbers)


# Etapa: Então o resultado deve ser exibido como {expected_result} na tela
@then("the result should be {expected_result:d} on the screen")
def step_impl(context, expected_result):
    """
    Etapa que verifica se o resultado exibido na tela é o esperado.

    Args:
        context: O objeto de contexto do Behave.
        expected_result: O resultado esperado.
    """
    assert (
        context.result == expected_result
    ), f"Expected {expected_result}, but got {context.result}"
