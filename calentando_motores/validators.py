from desafio import mimir

"""
Validadores para el desafio
"""


def mimir_checker():
    right = True
    checkers = [[False, False, True], [True, False, False],
                [False, True, True], [True, True, True]]

    for check in checkers:
        if mimir(check[0], check[1]) == check[2]:
            return "Correcto"
        else:
            return f"Oh no! mimir falló para dia_semana: {check[0]}, vacacion: {check[1]} no retornó {check[2]}"
            right = False
            break

    if right:
        return "Todo Correcto!"
