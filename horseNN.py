import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import matthews_corrcoef
import keras as keras

def Cargar_data():
	horse_data = pd.read_csv("datacarreras.csv")

	# Wins/Starts
	horse_data['effect_jinete'] = round(horse_data["jinete_gana"] / horse_data["jinete_act"] * 100, 2)
	horse_data['effect_trainer'] = round(horse_data["trainer_gana"] / horse_data["trainer_act"] * 100, 2)

	#Filtering and replacing values

	horse_data = horse_data.replace(np.inf, 30)
	horse_data = horse_data[horse_data.resultado != 0]
	horse_data["jinete_rep_mon"].replace(1, 0)
	horse_data["jinete_rep_mon"].replace(3, 1)

	print(horse_data.head())
	for col in horse_data.columns:
		print(col)

	carreras_1200 = horse_data.loc[horse_data['distancia_pista'] <= 1200]
	carreras_1200_gana = carreras_1200.loc[horse_data['resultado'] <= 5]
	carreras_1300_plus = horse_data.loc[horse_data['distancia_pista'] >=1300]
	carreras_1300_plus_gana = carreras_1300_plus.loc[horse_data['resultado'] <= 5]

	carreras_1200_gana["resultado_cat"] = pd.cut(carreras_1200_gana["resultado"], bins=[0., 1, 2, 3, 4, 5], labels=[1, 2, 3, 4, 5])
	carreras_1300_plus_gana["resultado_cat"] = pd.cut(carreras_1300_plus_gana["resultado"], bins=[0., 1, 2, 3, 4, 5], labels=[1, 2, 3, 4, 5])

	split = StratifiedShuffleSplit(n_splits=1, test_size=0.1, random_state=42)

	for train_index, test_index in split.split(carreras_1200_gana, carreras_1200_gana["resultado_cat"]):
		carreras_1200_train_strat = carreras_1200_gana.iloc[train_index]
		carreras_1200_test_strat = carreras_1200_gana.iloc[test_index]

	for train_index, test_index in split.split(carreras_1300_plus_gana, carreras_1300_plus_gana["resultado_cat"]):
		carreras_1300_train_strat = carreras_1300_plus_gana.iloc[train_index]
		carreras_1300_test_strat = carreras_1300_plus_gana.iloc[test_index]

	for set_ in (carreras_1200_train_strat, carreras_1200_test_strat):
		set_.drop("resultado_cat", axis=1, inplace=True)

	for set_ in (carreras_1300_train_strat, carreras_1300_test_strat):
		set_.drop("resultado_cat", axis=1, inplace=True)

	carreras_1200_r = carreras_1200_train_strat["resultado"].copy()
	carreras_1300_plus_r = carreras_1300_train_strat["resultado"].copy()

	carreras_1200_train_strat.drop("resultado", axis=1)
	carreras_1300_train_strat.drop("resultado", axis=1)

	carreras_1200_prepared = carreras_1200_train_strat[['tiempo', 'ult_div', 'posicion','cuerpos_ult', 'distancia_c', 'lote', 'jinete_gana', 'effect_jinete', 'jinete_rep_mon', 'trainer_gana','effect_trainer']]
	carreras_1300_prepared = carreras_1300_train_strat[['tiempo', 'ult_div', 'posicion','cuerpos_ult', 'distancia_c', 'lote', 'jinete_gana', 'effect_jinete', 'jinete_rep_mon', 'trainer_gana','effect_trainer']]

	transform_data = Pipeline([
		("scaler", StandardScaler())
	])

	#X_1200, y_1200 = carreras_1200_prepared, carreras_1200_r
	#X_1300, y_1300 = carreras_1300_prepared, carreras_1300_plus_r

	X_1200, X_1200_val, y_1200, y_1200_val = train_test_split(carreras_1200_prepared, carreras_1200_r, test_size=0.1)
	X_1300, X_1300_val, y_1300, y_1300_val = train_test_split(carreras_1300_prepared, carreras_1300_r, test_size=0.1)

	X_1200 = transform_data.fit_transform(X_1200)
	X_1300 = transform_data.fit_transform(X_1300)

	y_test_1200 = carreras_1200_test_strat["resultado"].copy()
	y_test_1300 = carreras_1300_test_strat["resultado"].copy()

	X_test_1200 = carreras_1200_test_strat[['tiempo', 'ult_div', 'posicion','cuerpos_ult', 'distancia_c', 'lote', 'jinete_gana', 'effect_jinete', 'jinete_rep_mon', 'trainer_gana','effect_trainer']]
	X_test_1300 = carreras_1300_test_strat[['tiempo', 'ult_div', 'posicion','cuerpos_ult', 'distancia_c', 'lote', 'jinete_gana', 'effect_jinete', 'jinete_rep_mon', 'trainer_gana','effect_trainer']]

	#X_test_1200_prepared = transform_data.fit_transform(X_test_1200)
	#X_test_1300_prepared = transform_data.fit_transform(X_test_1300)

	print(f"{X_1300.shape}")
	print(f"{y_1300.shape}")

	return X_1300, X_1300_val, X_test_1300, X_1200, X_1200_val, X_test_1200

def Grafica():
	pd.Dataframe(history.history).plot(figsize=(8, 5))
	plt.grid()
	plt.legend()
	plt.gca().set_ylim(1, 0)
	plt.show()

cargar_data = input("Cargar data? s/n: ")

if cargar_data == "s":
	Cargar_data()

cargar_modelo = input("Cargar Modelo? s/n: ")

if cargar_modelo == 's':
	model = keras.models.Sequential([
			keras.layers.Dense(50, activation="relu", input_shape=(11,)),
			#keras.layers.Dense(50, activation="selu", kernel_initializer="lecun_normal",input_shape=(11,)),
			#keras.layers.BatchNormalization(),
			keras.layers.Dropout(rate=0.2),
			keras.layers.Dense(5, activation="softmax"),
		]),

	model.compile(optimizer=keras.optimizers.SGD(lr=0.001, momentum=0.9, nesterov=True),
					loss=keras.losses.CategoricalCrossentropy(),
					metrics=["accuracy"])

	print(model.summary())

else:
	pass

entrenar_modelo = input("Entrenar modelo? s/n: ")

if entrenar_modelo == "s":
	history = model.fit(X_1300, y_1300, epoch=5,
						validation_data=(X_1300_val, y_1300_val),
						callbacks=[keras.callbacks.EarlyStopping(patience=12)])
	print("Done")

mostrar_grafica = input("Mostrar Grafico? s/n: ")

if mostrar_grafica == "s":
	Grafica()

evaluar_modelo = input("Evaluar modelo? s/n: ")

if evaluar_modelo == "s":
	print(model.evaluate(X_1300_test, y_1300_test))

	some_data = X_test_1300.iloc[:10]
	some_labels = y_test_1300.iloc[:10]

	y_proba = model.predict(some_data)

	print(f"{y_proba.round(2)}")
	print(f"Labels: {some_labels}")
