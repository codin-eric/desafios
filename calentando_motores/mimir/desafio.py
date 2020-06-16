"""
Este archivo contiene todas las funciones del desafio a mimir
"""


def mimir(dia_semana, vacacion):
    """
    El parametro dia_semana es True si estamos en un dia de la semana,
    el parametro vacacion es True si estamos en vacaciones. 
    Podemos mimir si no es dia de semana o si estamos en vacaciones.
    Devolver True si podemos mimir

    mimir(False, False) → True
    mimir(True, False) → False
    mimir(False, True) → True
    mimir(True, True) → True
    """
    print("not implemented")


# Validemos tu respuesta!
if __name__ == "__main__":
    """
    Descomentá el desafio que desees testear
    """

    right = True
    checkers = [[False, False, True], [True, False, False],
                [False, True, True], [True, True, True]]

    for check in checkers:
        if mimir(check[0], check[1]) == check[2]:
            res = "Correcto"
        else:
            res = f"Oh no! mimir falló para dia_semana: {check[0]}, vacacion: {check[1]} no retornó {check[2]}"
            right = False
            break

    if right:
        res = "Todo Correcto!"

    print(res)
