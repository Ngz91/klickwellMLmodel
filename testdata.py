import pandas as pd
import numpy as np
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import tensorflow as tf

dataf = pd.read_csv("./datacarreras.csv")
dataf["fecha"] = (
    dataf["fecha"].apply(lambda x: x.replace("-", "").strip()).astype(np.int64)
)
dataf.drop(labels='nombre_caballo', axis=1, inplace=True)
unique_fechas = dataf["fecha"].unique()
dataf = dataf.groupby(["fecha", "numero_carrera"])

def getRaces(dataframe, num_races):
    for i in np.array(num_races):
        for r in range(1, 13):
            try:
                df = dataframe.get_group((i, r))
                df = tf.convert_to_tensor(df, dtype=tf.float64)
                print(df)
            except KeyError:
                print(f"No data found for ID: {r}, Race num: {i}")

getRaces(dataf, unique_fechas[:3])
