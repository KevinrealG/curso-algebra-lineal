"""Laboratorio 8: misión monedas en R3 con Python."""

from fractions import Fraction
from typing import Iterable


Vector = tuple[Fraction, ...]


def vector(*components: int) -> Vector:
    return tuple(Fraction(component) for component in components)


def linear_combination(
    vectors: tuple[Vector, Vector, Vector],
    coefficients: tuple[int, int, int],
) -> Vector:
    """Calcula a*v1 + b*v2 + c*v3."""
    return tuple(
        coefficients[0] * vectors[0][row]
        + coefficients[1] * vectors[1][row]
        + coefficients[2] * vectors[2][row]
        for row in range(3)
    )


def matrix(vectors: tuple[Vector, Vector, Vector]) -> list[list[Fraction]]:
    """Construye la matriz A = [v1 v2 v3]."""
    return [[vectors[column][row] for column in range(3)] for row in range(3)]


def gauss_jordan(matrix_a: list[list[Fraction]], P: Vector) -> tuple[list[list[Fraction]], list[Fraction] | None]:
    """Resuelve Ax = P y también retorna la matriz aumentada."""
    augmented = [row[:] + [P[row_index]] for row_index, row in enumerate(matrix_a)]

    row_count = 3
    pivot_row = 0
    for column in range(3):
        pivot = next(
            (row for row in range(pivot_row, row_count) if augmented[row][column] != 0),
            None,
        )
        if pivot is None:
            continue

        augmented[pivot_row], augmented[pivot] = augmented[pivot], augmented[pivot_row]
        pivot_value = augmented[pivot_row][column]
        augmented[pivot_row] = [value / pivot_value for value in augmented[pivot_row]]

        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = augmented[row][column]
            augmented[row] = [
                augmented[row][index] - factor * augmented[pivot_row][index]
                for index in range(4)
            ]
        pivot_row += 1

    for row in augmented:
        if all(value == 0 for value in row[:3]) and row[3] != 0:
            return augmented, None

    if pivot_row < 3:
        return augmented, None

    solution = [augmented[row][3] for row in range(3)]
    return augmented, solution


def determinant3(matrix_a: list[list[Fraction]]) -> Fraction:
    a, b, c = matrix_a[0]
    d, e, f = matrix_a[1]
    g, h, i = matrix_a[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def integer_nonnegative(solution: list[Fraction] | None) -> bool:
    return solution is not None and all(
        value.denominator == 1 and value >= 0 for value in solution
    )


def format_vector(value: Iterable[Fraction]) -> str:
    return "(" + ", ".join(str(component) for component in value) + ")"


def analyze_base(vectors: tuple[Vector, Vector, Vector], objectives: dict[str, Vector]) -> None:
    matrix_a = matrix(vectors)
    det = determinant3(matrix_a)

    print("\nMatriz A:")
    for row in matrix_a:
        print(format_vector(row))
    print("det(A) =", det)
    print("¿Es una base?", "Sí" if det != 0 else "No")

    for name, position in objectives.items():
        augmented, solution = gauss_jordan(matrix_a, position)
        coefficients = (
            tuple(int(value) for value in solution)
            if integer_nonnegative(solution)
            else solution
        )
        reachable = integer_nonnegative(solution)

        print(f"\n{name}: P = {format_vector(position)}")
        print("Matriz aumentada:")
        for row in augmented:
            print(format_vector(row[:3]) + " | " + str(row[3]))
        print("Solución (a, b, c):", coefficients)
        print("Clasificación:", "ALCANZABLE" if reachable else "NO ALCANZABLE")

        if reachable:
            print("Pulsaciones:", coefficients)


def demonstrate_recommended_usage() -> None:
    original_vectors = (
        vector(1, 1, 0),
        vector(1, 0, 1),
        vector(0, 1, 1),
    )
    original_objectives = {
        "Moneda 1": vector(3, 3, 2),
        "Moneda 2": vector(3, 2, 3),
        "Moneda 3": vector(1, 1, 1),
    }

    print("=== ETAPA 1: ANÁLISIS AUTOMÁTICO ===")
    analyze_base(original_vectors, original_objectives)

    print("\n=== ETAPA 2: NUEVAS POSICIONES ===")
    new_coefficients = ((2, 0, 1), (1, 2, 2), (0, 3, 1), (3, 1, 1))
    new_objectives: dict[str, Vector] = {}
    for index, coefficients in enumerate(new_coefficients, start=1):
        position = linear_combination(original_vectors, coefficients)
        new_objectives[f"Objetivo nuevo {index}"] = position
        print(
            f"{coefficients} -> "
            f"P = {format_vector(position)}"
        )
    analyze_base(original_vectors, new_objectives)

    print("\n=== ETAPA 3: NUEVA BASE ===")
    proposed_vectors = (
        vector(1, 0, 1),
        vector(0, 2, 1),
        vector(1, 1, 0),
    )
    proposed_objectives = {
        "Objetivo A": linear_combination(proposed_vectors, (2, 1, 0)),
        "Objetivo B": linear_combination(proposed_vectors, (0, 2, 3)),
        "Objetivo C": linear_combination(proposed_vectors, (1, 0, 4)),
    }
    analyze_base(proposed_vectors, proposed_objectives)

    print("\n=== EXPERIMENTO DE CONTROL ===")
    dependent_vectors = (
        proposed_vectors[0],
        proposed_vectors[1],
        (
            proposed_vectors[0][0] + proposed_vectors[1][0],
            proposed_vectors[0][1] + proposed_vectors[1][1],
            proposed_vectors[0][2] + proposed_vectors[1][2],
        ),
    )
    analyze_base(
        dependent_vectors,
        {"Punto de prueba": vector(1, 1, 1)},
    )


def main() -> None:
    print("Laboratorio 8 - Misión monedas en R3")
    print("Ejecute las funciones analyze_base() y linear_combination()")
    print("desde su propio programa para modificar los datos.")
    demonstrate_recommended_usage()


if __name__ == "__main__":
    main()
