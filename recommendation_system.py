def calcular_imc(peso_kg: float, altura_m: float) -> float:
    """Calcula el índice de masa corporal (IMC) a partir del peso y la altura."""
    if peso_kg <= 0 or altura_m <= 0:
        raise ValueError("El peso y la altura deben ser mayores que cero.")

    return peso_kg / (altura_m**2)


def calcular_indice_masa_muscular(
    masa_muscular_kg: float, altura_m: float
) -> float:
    """Calcula el índice de masa muscular: masa muscular (kg) / altura (m)²."""
    if masa_muscular_kg <= 0 or altura_m <= 0:
        raise ValueError(
            "La masa muscular y la altura deben ser mayores que cero."
        )

    return masa_muscular_kg / (altura_m**2)