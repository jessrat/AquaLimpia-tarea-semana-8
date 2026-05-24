# validaciones.py

def validar_columnas(df, columnas_requeridas):
    faltantes = [col for col in columnas_requeridas if col not in df.columns]

    if faltantes:
        print(f" Columnas faltantes: {faltantes}")
        return False
    
    print(" Todas las columnas necesarias están presentes")
    return True


def validar_valores_negativos(df, columnas):
    problemas = {}

    for col in columnas:
        negativos = (df[col] < 0).sum()
        if negativos > 0:
            problemas[col] = negativos

    if problemas:
        print(" Se encontraron valores negativos:")
        print(problemas)
    else:
        print(" No hay valores negativos")

    return problemas



def analizar_calidad_datos(df):

    print("\n--- ANALISIS DE CALIDAD DE DATOS ---")

    # 1. Valores nulos reales
    print("\nValores nulos por columna:")
    print(df.isnull().sum())

    # 2. Valores vacíos tipo string
    vacios = df.applymap(lambda x: isinstance(x, str) and x.strip() == "").sum()
    print("\nValores vacíos (strings):")
    print(vacios)

    # 3. Tipos de datos
    print("\nTipos de datos:")
    print(df.dtypes)

    # 4. Duplicados
    duplicados = df.duplicated().sum()
    print(f"\nRegistros duplicados: {duplicados}")

    print("\n--- FIN ANALISIS ---")