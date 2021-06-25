
Klickwell Machine Learning and NN model
=======================================

Description
===========

After compiling some data about horse races in Venezuela, analysing, cleaning and transforming the data, I decided to build and test 2 models that could predict the outcome of a race, or at least get close to the real result. The database is available for download as a csv file, although, there might be some data missing about some races or the horses. Inside the notebook there's a full description of the steps taken. Some of them might change overtime as i'm still working in this project.

Authors
=======

Nevio Gomez, 2020

Requirements
============

* Python 3
* Jupyter notebook (can be open in google colab)
* Pandas
* Numpy
* Matplotlib
* Scikit-Learn
* Keras 2.3.0 (Tested with Theano, Tensorflow can be used)

Notes
=====

Dataset of Venezuelan horse racing, collected and arranged by my father and i in our spare time, we update it almost every month with new data. (Due to problems with my main computer, the database will not be updated for some time or until i can recover the data from my main computer)

Description of the features:
- Fecha: Date of the race 
- numero_carrera: Number of the race for that date
- distancia_pista: Distance of the track
- grupo: Group of horses, 1 for no winners, 2 for winners of 1...until 7 for Classics
- nombre_caballo: Name of the horse
- tiempo: Time of the horse in past races for that distance (adjusted)
- ult_div: dividend, how much the horse paid on the last race
- penult_div: dividend for the race before the last one
- posicion: standing of the horse in the last race
- cuerpos_ult: bodies for the last race
- cuerpos_penult: bodies for the race before the last one
- distancia_c: If the horse ran in the distance before (diferent judgement for short and long races)
- lote: if the horse already ran in no winners, winners of 1, etc. 4 means the horse its gonna run in a lower group
(E.g, from a classic to a winners of 3 race)
- jinete_act, jinete_gan, trainer_act, trainer_gan: startups of the jockey/trainer, wins of the jockey/trainer
- jinete_rep_mon: if the jockey repeats the horse
- resultados: results
