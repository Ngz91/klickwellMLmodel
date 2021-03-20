# klickwellMLmodel

Building Machine learning and neural networks models to predict the winner out of five horses.
An attempt to rearrange the results given by the Klickwell method.

Dataset of Venezuelan horse racing, collected and arranged by my father and i in our spare time, we ipdate it 
almost every month with new data.

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
