import pandas as pd

def games_by_year(df: pd.DataFrame) -> pd.DataFrame:
    """Resume cantidad de lanzamientos y ventas globales por año de lanzamiento."""
    valid_years = df.dropna(subset=["year_of_release"]).copy()
    summary = (
        valid_years.groupby("year_of_release", as_index=False)
        .agg(
            games_released=("name", "count"),
            total_sales=("total_sales", "sum"),
        )
        .sort_values("year_of_release")
        .reset_index(drop=True)
    )
    return summary


def platform_sales_by_year(df: pd.DataFrame, top_n: int | None = None) -> pd.DataFrame:
    """Construye una tabla de ventas globales por año y plataforma."""
    valid = df.dropna(subset=["year_of_release", "platform"]).copy()
    if top_n is not None:
        top_platforms = (
            valid.groupby("platform")["total_sales"]
            .sum()
            .nlargest(top_n)
            .index
        )
        valid = valid[valid["platform"].isin(top_platforms)]

    pivot = valid.pivot_table(
        index="year_of_release",
        columns="platform",
        values="total_sales",
        aggfunc="sum",
        fill_value=0.0,
    ).sort_index()
    return pivot


def platform_lifespan_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula año inicial, año final, duración y ventas totales por plataforma."""
    valid = df.dropna(subset=["year_of_release", "platform"]).copy()
    summary = (
        valid.groupby("platform", as_index=False)
        .agg(
            first_year=("year_of_release", "min"),
            last_year=("year_of_release", "max"),
            total_games=("name", "count"),
            total_sales=("total_sales", "sum"),
        )
    )
    summary["lifespan_years"] = (summary["last_year"] - summary["first_year"] + 1).astype("Int64")
    return summary.sort_values("total_sales", ascending=False).reset_index(drop=True)

def retired_platforms_summary(df: pd.DataFrame) -> tuple[int, pd.DataFrame]:
    """Devuelve el último año del dataset y las plataformas sin ventas en ese año."""
    lifespan_df = platform_lifespan_summary(df)
    max_year = int(df["year_of_release"].max())
    retired_df = (
        lifespan_df[lifespan_df["last_year"] < max_year]
        .sort_values("total_sales", ascending=False)
        .reset_index(drop=True)
    )
    return max_year, retired_df

def filter_analysis_period(
    df: pd.DataFrame,
    start_year: int = 2013,
    end_year: int = 2016,
) -> pd.DataFrame:
    """Filtra el dataset al rango de años seleccionado para proyectar el año siguiente."""
    valid = df.dropna(subset=["year_of_release"]).copy()
    mask = (valid["year_of_release"] >= start_year) & (valid["year_of_release"] <= end_year)
    return valid.loc[mask].reset_index(drop=True)


def period_platform_summary(period_df: pd.DataFrame) -> pd.DataFrame:
    """Calcula ventas totales, promedio, mediana y juegos lanzados por plataforma en el período."""
    summary = (
        period_df.groupby("platform", as_index=False)
        .agg(
            games_count=("name", "count"),
            total_sales=("total_sales", "sum"),
            mean_sales=("total_sales", "mean"),
            median_sales=("total_sales", "median"),
        )
        .sort_values("total_sales", ascending=False)
        .reset_index(drop=True)
    )
    return summary

def score_sales_correlation(
    period_df: pd.DataFrame,
    platform: str,
) -> dict[str, float | int]:
    """Calcula correlaciones de Pearson entre critic_score / user_score y total_sales en una plataforma."""
    plat_df = period_df[period_df["platform"] == platform].copy()

    critic_sub = plat_df.dropna(subset=["critic_score", "total_sales"])
    user_sub = plat_df.dropna(subset=["user_score", "total_sales"])

    return {
        "platform": platform,
        "critic_n": int(len(critic_sub)),
        "critic_corr": float(critic_sub["critic_score"].corr(critic_sub["total_sales"])),
        "user_n": int(len(user_sub)),
        "user_corr": float(user_sub["user_score"].corr(user_sub["total_sales"])),
    }


def genre_sales_summary(period_df: pd.DataFrame) -> pd.DataFrame:
    """Resume cantidad de juegos, ventas totales, promedio y mediana por género."""
    valid = period_df.dropna(subset=["genre"]).copy()
    summary = (
        valid.groupby("genre", as_index=False)
        .agg(
            games_count=("name", "count"),
            total_sales=("total_sales", "sum"),
            mean_sales=("total_sales", "mean"),
            median_sales=("total_sales", "median"),
        )
        .sort_values("total_sales", ascending=False)
        .reset_index(drop=True)
    )
    summary["share_of_sales_pct"] = (summary["total_sales"] / summary["total_sales"].sum() * 100).round(2)
    return summary

REGION_COLS: dict[str, str] = {
    "NA": "na_sales",
    "EU": "eu_sales",
    "JP": "jp_sales",
}


def top_items_by_region(
    period_df: pd.DataFrame,
    dimension: str,
    top_n: int = 5,
) -> dict[str, pd.DataFrame]:
    """Devuelve el top_n de una dimensión ('platform' o 'genre') por región con ventas y cuota (%)."""
    result: dict[str, pd.DataFrame] = {}
    valid = period_df.dropna(subset=[dimension]).copy()

    for region, col in REGION_COLS.items():
        region_total = valid[col].sum()
        grouped = (
            valid.groupby(dimension, as_index=False)[col]
            .sum()
            .rename(columns={col: "sales"})
            .sort_values("sales", ascending=False)
            .head(top_n)
            .reset_index(drop=True)
        )
        grouped["market_share_pct"] = (
            (grouped["sales"] / region_total * 100).round(2) if region_total > 0 else 0.0
        )
        result[region] = grouped

    return result


def esrb_sales_by_region(period_df: pd.DataFrame) -> pd.DataFrame:
    """Resume ventas totales, promedio y juegos lanzados por clasificación ESRB en NA, EU y JP."""
    temp = period_df.copy()
    temp["rating"] = temp["rating"].fillna("Sin clasificación (NaN)")

    summary = (
        temp.groupby("rating", as_index=False)
        .agg(
            games_count=("name", "count"),
            na_sales=("na_sales", "sum"),
            eu_sales=("eu_sales", "sum"),
            jp_sales=("jp_sales", "sum"),
            na_mean=("na_sales", "mean"),
            eu_mean=("eu_sales", "mean"),
            jp_mean=("jp_sales", "mean"),
        )
        .sort_values("na_sales", ascending=False)
        .reset_index(drop=True)
    )
    return summary