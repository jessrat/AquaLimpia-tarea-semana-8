import matplotlib.pyplot as plt

def grafico_caudal_promedio(df):

    caudal_promedio = df.groupby("planta")["caudal_entrada_m3_d"].mean()

    fig, ax = plt.subplots(figsize=(8,5))
    caudal_promedio.plot(kind="bar", ax=ax)

    ax.set_title("Caudal Promedio por Planta")
    ax.set_xlabel("Planta")
    ax.set_ylabel("Caudal (m3/d)")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()


def grafico_cumplimiento(df):

    cumplimiento = df.groupby("planta")["cumplimiento_norma"].mean() * 100

    fig, ax = plt.subplots(figsize=(8,5))
    cumplimiento.plot(kind="bar", ax=ax)

    ax.set_title("Cumplimiento (%) por Planta")
    ax.set_xlabel("Planta")
    ax.set_ylabel("Cumplimiento (%)")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()