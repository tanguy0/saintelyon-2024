import pandas as pd


def clean_athlete_names(name: str) -> str:
    prefix = "♀\r\n"
    if name.startswith(prefix):
        return name[len(prefix):]
    return name


def extract_sexe_from_categorie(name: str) -> str:
    if name.endswith("H"):
        return "H"
    return "F"


def time_to_seconds(time_str: str) -> int:
    h, m, s = map(int, time_str.split(":"))
    return int(h * 3600 + m * 60 + s)


def seconds_to_time(seconds: int) -> list:
    h = seconds//3600
    seconds = seconds%3600
    m = seconds//60
    s = seconds%60
    return [h, m, s]


def find_x_closest_y(
    x: str, 
    y: str, 
    row: pd.DataFrame, 
    data: pd.DataFrame
) -> pd.DataFrame:
    closest_row = data.iloc[(data[y] - row[y]).abs().argmin()]
    return closest_row[x]