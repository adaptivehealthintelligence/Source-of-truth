import pandas as pd
from typing import Iterator


def import_excel(path: str) -> pd.DataFrame:
    # return pd.read_excel('SampleWork.xlsx')
    return pd.read_excel(path)


def df_to_cypher(df: pd.DataFrame, label: str, id_field: str = "id") -> str:
    # return
    # CREATE
    # (james:Person {name: "James Totterdell", position: "Biostatistician"}),
    # (mark:Person {name: "Mark Jones", position: "Biostatistician"}),
    # (tom:Person {name: 'Tom Snelling', position: "Director"}),
    # (reena:Person {name: "Reena D'Souza", email: "Reena.D'Souza@telethonkids.org.au"} ),
    # (todd:Person {name: 'Todd "Cooper"', age: 30, height: 1.8, dob: date("1968-04-26")}),

    # (motc:Project {title: "Motivate-C"}),
    # (mfit:Project {title: "M-FIT"})

    if id_field not in df.columns:
        raise ValueError(f"DataFrame must contain the ID column named '{id_field}'")

    col_map = {col: str(df[col].dtype) for col in df.columns}

    def rec_to_str(rec) -> str:
        fld_strs = []
        for col, col_type in col_map.items():
            if col == id_field:
                continue
            match col_type:
                case "int64":
                    fld_strs.append(f"{col}: toInteger({rec[col]})")
                case "float64":
                    fld_strs.append(f"{col}: toFloat({rec[col]})")
                case "datetime64[ns]":
                    dt_str = rec[col].date()
                    fld_strs.append(f'{col}: date("{dt_str}")')
                case _:
                    # usually object which means string
                    fld_strs.append(f'{col}: "{rec[col]}"')

        # format = (id:Label {attrib1: "value1", attrib2: "value2"})
        # EG     = (tom:Person {name: 'Tom Snelling', position: "Director"}),
        return f"({rec[id_field]}:{label} {{{', '.join(fld_strs)}}})"

    rec_strs = [rec_to_str(rec) for rec in df.to_dict(orient="records")]

    return f"CREATE\n{',\n'.join(rec_to_str(rec) for rec in df.to_dict(orient='records'))}\n"

    # CREATE (edward:Person {name: "Edward Pan", position: "Statistical Programmer"})
    # for record in df.to_dict(orient="records"):
    #     attrib_str = ", ".join([f'{k}: "{v}"' for k, v in record.items()])
    #     yield f"CREATE (n:{label} {record})"
    # return f"CREATE (n:{label} {df.to_dict(orient='records')[0]})"
