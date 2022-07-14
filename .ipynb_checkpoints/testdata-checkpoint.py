from typing import List
import pandas as pd
import numpy as np
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import tensorflow as tf

dataf = pd.read_csv("./datacarreras.csv")
dataf["fecha"] = (
    dataf["fecha"].apply(lambda x: x.replace("-", "").strip()).astype(np.int64)
)

unique_fechas = dataf["fecha"].unique()
dataf = dataf.groupby(["fecha", "numero_carrera"])
"""
c1_data = dataf.get_group((4042021, 1)) 


print(c1_data.to_numpy())

c1_data = c1_data.drop(["nombre_caballo"], axis=1)
c1_data = tf.convert_to_tensor(c1_data, dtype=tf.float64)

print(c1_data)
"""

def getRaces(dataframe: pd.DataFrame, num_races: List):
    for r in np.array(num_races):
        for i in range(1, 13):
            try:
                df = dataframe.get_group((i, r))
                df = dataframe.drop(["nombre_caballo"], axis=1)
                df = tf.convert_to_tensor(df, dtype=tf.float64)
                print(df)
            except KeyError:
                print(f"No data found for ID: {r}, Race num: {i}")
