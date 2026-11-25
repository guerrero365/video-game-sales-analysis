from pathlib import Path
import numpy as np
import pandas as pd


def get_project_root() -> Path:
    """Devuelve la ruta raíz del proyecto tanto en scripts (.py) como en notebooks."""
    if "__file__" in globals():
        return Path(__file__).resolve().parents[1]
    cwd = Path.cwd()
    return cwd.parent if cwd.name == "notebooks" else cwd


def load_raw_games(filename: str = "games.csv") -> pd.DataFrame:
    """Carga el dataset histórico de videojuegos desde data/raw/."""
    csv_path = get_project_root() / "data" / "raw" / filename
    return pd.read_csv(csv_path)


def clean_and_prepare_games(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia nombres de columnas, convierte tipos de datos, trata 'TBD'
    como valor faltante y calcula la columna de ventas globales (total_sales).
    """
    data = df.copy()

    # 1. Normalizar nombres de columnas a minúsculas sin espacios externos
    data.columns = data.columns.str.strip().str.lower()

    # 2. Convertir 'TBD' en user_score a NaN y castear a numérico
    data["user_score"] = data["user_score"].replace("TBD", np.nan)
    data["user_score"] = pd.to_numeric(data["user_score"], errors="coerce")

    # 3. Convertir critic_score a numérico y year_of_release a entero nullable (Int64)
    data["critic_score"] = pd.to_numeric(data["critic_score"], errors="coerce")
    data["year_of_release"] = pd.to_numeric(data["year_of_release"], errors="coerce").astype("Int64")

    # 4. Estandarizar columnas de texto/categoría preservando valores ausentes
    for col in ["name", "platform", "genre", "rating"]:
        if col in data.columns:
            data[col] = data[col].astype("string").str.strip()

    # 5. Calcular ventas totales en millones de USD sumando todas las regiones
    sales_cols = ["na_sales", "eu_sales", "jp_sales", "other_sales"]
    data["total_sales"] = data[sales_cols].sum(axis=1)

    # 6. Revisar y eliminar duplicados exactos si existieran
    exact_duplicates = data.duplicated().sum()
    if exact_duplicates > 0:
        data = data.drop_duplicates().reset_index(drop=True)

    # 7. Eliminar registros sin nombre de juego (2 filas anónimas de 1993)
    data = data.dropna(subset=["name"]).copy()

    # 8. Corregir año faltante en el registro partido de Sonic the Hedgehog (PS3, 2006)
    mask_sonic_na = (
        (data["name"] == "Sonic the Hedgehog")
        & (data["platform"] == "PS3")
        & (data["year_of_release"].isna())
    )
    data.loc[mask_sonic_na, "year_of_release"] = 2006

    # 9. Consolidar registros partidos que comparten (name, platform, year_of_release)
    # Preserva remakes/reboots en años distintos (ej. Need for Speed: Most Wanted 2005 vs 2012)
    group_cols = ["name", "platform", "year_of_release"]
    has_year = data["year_of_release"].notna()

    consolidated = (
        data[has_year]
        .groupby(group_cols, as_index=False, dropna=False)
        .agg({
            "genre": "first",
            "na_sales": "sum",
            "eu_sales": "sum",
            "jp_sales": "sum",
            "other_sales": "sum",
            "critic_score": "first",
            "user_score": "first",
            "rating": "first",
        })
    )

    data = pd.concat([consolidated, data[~has_year]], ignore_index=True)

    # 10. Recalcular ventas globales tras consolidar
    sales_cols = ["na_sales", "eu_sales", "jp_sales", "other_sales"]
    data["total_sales"] = data[sales_cols].sum(axis=1)

    return data