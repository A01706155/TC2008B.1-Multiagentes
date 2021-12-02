from flask import Flask, render_template, request, jsonify
import json, logging, os, atexit

# Importamos las clases que se requieren para manejar los agentes (Agent) y su entorno (Model).
from mesa import Agent, Model

# Con ''RandomActivation'' hacemos que todos los agentes se activen al mismo tiempo
from mesa.time import RandomActivation

# Utilizaremos ''DataCollector'' para obtener información de cada paso de la simulación
from mesa.datacollection import DataCollector

# matplotlib se usa para crear la animación
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.rcParams["animation.html"] = "jshtml"
matplotlib.rcParams['animation.embed_limit'] = 2**128

#Importamos los siguientes paquetes para el mejor manejo de valores numéricos
import numpy as np
import pandas as pd

from RetoAgentes import Semaforo, CajaControl, Carro, CarreteraModel

app = Flask(__name__, static_url_path='')

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8045))

# Número de carros
carros = 20

# Duración máxima de la animación
DURACION = 70

model = CarreteraModel(carros)

for i in range(DURACION):
        model.step()

@app.route('/')
def root():
        var = model.datacollector.get_model_vars_dataframe()
        return jsonify(str(var))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)