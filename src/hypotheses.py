from __future__ import annotations

from dataclasses import dataclass
import pandas as pd
from scipy import stats


@dataclass
class HypothesisResult:
    test_name: str
    group_a_label: str
    group_b_label: str
    n_a: int
    n_b: int
    mean_a: float
    mean_b: float
    var_a: float
    var_b: float
    t_stat: float
    p_value: float
    alpha: float
    equal_var: bool
    reject_null: bool


def compare_user_scores(
    df: pd.DataFrame,
    column: str,
    group_a: str,
    group_b: str,
    test_name: str,
    alpha: float = 0.05,
    equal_var: bool = False,
) -> HypothesisResult:
    """Compara user_score promedio entre dos categorías de una columna ('platform' o 'genre')."""
    sub = df.dropna(subset=[column, "user_score"]).copy()

    scores_a = sub.loc[sub[column] == group_a, "user_score"].astype(float)
    scores_b = sub.loc[sub[column] == group_b, "user_score"].astype(float)

    t_stat, p_value = stats.ttest_ind(scores_a, scores_b, equal_var=equal_var)

    return HypothesisResult(
        test_name=test_name,
        group_a_label=group_a,
        group_b_label=group_b,
        n_a=int(len(scores_a)),
        n_b=int(len(scores_b)),
        mean_a=float(scores_a.mean()),
        mean_b=float(scores_b.mean()),
        var_a=float(scores_a.var(ddof=1)),
        var_b=float(scores_b.var(ddof=1)),
        t_stat=float(t_stat),
        p_value=float(p_value),
        alpha=alpha,
        equal_var=equal_var,
        reject_null=bool(p_value < alpha),
    )


def results_to_dataframe(results: list[HypothesisResult]) -> pd.DataFrame:
    """Convierte una lista de resultados de pruebas de hipótesis en un DataFrame resumen."""
    rows = [
        {
            "prueba": r.test_name,
            "grupo_a": r.group_a_label,
            "n_a": r.n_a,
            "media_a": round(r.mean_a, 3),
            "grupo_b": r.group_b_label,
            "n_b": r.n_b,
            "media_b": round(r.mean_b, 3),
            "t_stat": round(r.t_stat, 4),
            "p_value": f"{r.p_value:.4e}" if r.p_value < 0.0001 else round(r.p_value, 4),
            "alpha": r.alpha,
            "rechaza_h0": r.reject_null,
        }
        for r in results
    ]
    return pd.DataFrame(rows)