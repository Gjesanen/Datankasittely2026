from pathlib import Path

from dagster_duckdb import DuckDBResource

import dagster as dg

database_path = Path(__file__).resolve().parents[3] / "jaffle_platform.duckdb"
database_resource = DuckDBResource(database=str(database_path))


@dg.definitions
def resources():
    return dg.Definitions(
        resources={
            "duckdb": database_resource,
        }
    )