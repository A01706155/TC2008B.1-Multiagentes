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

# Agente semáforos que usaremos
class Semaforo(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        
        # Inicia en luz roja
        self.light = False

# Agente de la caja de control
class CajaControl(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        
        self.model = model
        self.temp = 10
        
        # Cuenta los carros de las filas y cambia los semáfors dependiendo de los carros
        self.contarCarros()
        self.cambiarSemLuz()        
        
        
    def step(self):
        self.contarCarros()
        
        if self.temp == 0:
            self.cambiarSemLuz()
            self.temp = 10
            
        self.temp -= 1
            
    
    # Cuenta los carros de cada fila 
    def contarCarros(self):
        self.total_norte = 0
        self.total_sur = 0
        self.total_este = 0
        self.total_oeste = 0
        
        for agent in self.model.schedule.agents:
            if agent.orientation == 'inicioNorte':
                self.total_norte += 1
            
            elif agent.orientation == 'inicioSur':
                self.total_sur += 1
            
            elif agent.orientation == 'inicioEste':
                self.total_este += 1
            
            elif agent.orientation == 'inicioOeste':
                self.total_oeste += 1

    # Cambia el color del semáforo a verde dependiendo de cuantos carros haya    
    def cambiarSemLuz(self):
        # Semáforo de arriba
        if(self.total_norte == max(self.total_norte ,max(self.total_sur, max(self.total_este, self.total_oeste)))):
            self.model.semNorte.light = True            
            self.model.semEste.light = False
            self.model.semOeste.light = False  
            self.model.semSur.light = False
        
        # Semáforo de la derecha
        elif(self.total_este == max(self.total_norte, max(self.total_sur, max(self.total_este, self.total_oeste)))):
            self.model.semNorte.light = False            
            self.model.semEste.light = True
            self.model.semOeste.light = False
            self.model.semSur.light = False            
        
        # Semáforo de la izquierda
        elif(self.total_oeste == max(self.total_norte, max(self.total_sur,max(self.total_este,self.total_oeste)))):
            self.model.semNorte.light = False            
            self.model.semEste.light = False
            self.model.semOeste.light = True
            self.model.semSur.light = False
        
        # Semáforo de abajo
        elif(self.total_sur == max(self.total_norte, max(self.total_sur, max(self.total_este, self.total_oeste)))):
            self.model.semNorte.light = False            
            self.model.semEste.light = False
            self.model.semOeste.light = False
            self.model.semSur.light = True

class Carro(Agent):
    def __init__(self, unique_id, model, x, y, orientation):
        super().__init__(unique_id, model)
        self.model = model
        
        # Orientación del carro
        self.orientation = orientation
        
        # Posición del carro
        self.position = np.array((x,y), dtype=np.float64)
        
        # Velocidad del carro
        self.asignarVelocidad()
                
        #variables para la vuelta
        self.index = 0
        self.turn = False
        
        # Distancia entre los carros
        self.dist_carros = 0.8
        
    
    def step(self):
        # Se le asigna una velocidad inicial
        self.asignarVelocidad()
        
        # El carro sigue la trayectoria
        if self.frenar() == False:
            self.vuelta()
            
            if self.turn == True:
                
                if self.index < len(self.curve):
                    self.position = self.curve[self.index]
                    self.index += 1

                else:
                    self.turn = False
                    self.index = 0
            
            elif self.turn == False:
                self.position = self.position + self.velocity
     
    # Hace que el carro frene si la luz del semáforo esta en rojo
    def frenar(self):
        if self.orientation == 'inicioEste' and self.position.flatten()[0] == 3: 
            if self.model.semEste.light == False:
                return True

        elif self.orientation == 'inicioNorte' and self.position.flatten()[1] == 3:
            if self.model.semNorte.light == False:
                return True

        elif self.orientation == 'inicioOeste' and self.position.flatten()[0] == -3:
            if self.model.semOeste.light == False:
                return True

        elif self.orientation == 'inicioSur' and self.position.flatten()[1] == -3:
            if self.model.semSur.light == False:
                return True
        
        if self.revisaCarros() == True:
            return True
        
        return False

    # Le asigna la velocidad a los carros dependiendo de su dirección
    def asignarVelocidad(self):       
        if self.orientation == 'inicioEste':
            vel = -1
            self.velocity = np.array((vel, 0), dtype=np.float64)
            
        elif self.orientation == 'inicioNorte':
            vel = -1
            self.velocity = np.array((0, vel), dtype=np.float64)

        elif self.orientation == 'inicioOeste':
            vel = 1
            self.velocity = np.array((vel, 0), dtype=np.float64)

        elif self.orientation == 'inicioSur':
            vel = 1
            self.velocity = np.array((0, vel), dtype=np.float64)
        
    
    # Revisa si hay otros carros delante 
    def revisaCarros(self):
        for agent in self.model.schedule.agents:
            
            # Carriles de la derecha
            if self.orientation == 'inicioEste':
                if self.position[1] == 0:
                    if self.position[0] - 1 == agent.position[0] and self.position[1] - agent.position[1] == 0:
                        return True
 
                elif self.position[1] == 2:
                    if self.position[0] - 1 == agent.position[0] and self.position[1] - agent.position[1] == 0:
                        return True
            
            # Carriles de la izquierda
            elif self.orientation == 'inicioOeste':
                if self.position[1] == 0:
                    if self.position[0] + 1 == agent.position[0] and self.position[1] - agent.position[1] == 0:
                        return True
                    
                elif self.position[1] == -2:
                    if self.position[0] + 1 == agent.position[0] and self.position[1] - agent.position[1] == 0:
                        return True

            # Carriles de arriba
            elif self.orientation == 'inicioNorte':
                if self.position[0] == 0:
                    if self.position[1] - 1 == agent.position[1] and self.position[0] - agent.position[0] == 0:
                        return True

                elif self.position[0] == -2:
                    if self.position[1] - 1 == agent.position[1] and self.position[0] - agent.position[0] == 0:
                        return True
            
            # Carriles de abajo
            elif self.orientation == 'inicioSur':
                if self.position[0] == 0:
                    if self.position[1] + 1 == agent.position[1] and self.position[0] - agent.position[0] == 0:
                        return True

                elif self.position[0] == 2:
                    if self.position[1] + 1 == agent.position[1] and self.position[0] - agent.position[0] == 0:
                        return True
            
        return False

    # Da la vuelta a la derecha o izquierda si es que es posible
    def vuelta(self):
        choice = np.random.choice([True,False])
        
        # Hacia la derecha
        if self.orientation == 'inicioEste' and self.position.flatten()[0] == 3 and self.position.flatten()[1] == 2: 
            if choice == True:
                self.curve = np.array([[2.68,2.05], [2.4,2.17], [2.2,2.39], [2.06,2.67]])
                self.turn = True
                self.orientation = 'inicioSur'
            
        elif self.orientation == 'inicioSur' and self.position.flatten()[0] == 2 and self.position.flatten()[1] == -3: 
            if choice == True:
                self.curve = np.array([[2.05,-2.7], [2.22,-2.42], [2.45,-2.23], [2.72,-2.06]])
                self.turn = True
                self.orientation = 'inicioOeste'
            
        elif self.orientation == 'inicioOeste' and self.position.flatten()[0] == -3 and self.position.flatten()[1] == -2: 
            if choice == True:
                self.curve = np.array([[-2.7,-2.08], [-2.46,-2.26], [-2.26,-2.47], [-2.11,-2.73]])
                self.turn = True
                self.orientation = 'inicioNorte'
            
        elif self.orientation == 'inicioNorte' and self.position.flatten()[0] == -2 and self.position.flatten()[1] == 3: 
            if choice == True:
                self.curve = np.array([[-2.05,2.7], [-2.22,2.42], [-2.45,2.23], [-2.72,2.06]])
                self.turn = True
                self.orientation = 'inicioEste'

        # Hacia la izquierda
        if self.orientation == 'inicioEste' and self.position.flatten()[0] == 3 and self.position.flatten()[1] == 0:
            self.curve = np.array([[2.38,-0.24], [1.74,-0.5], [1.01,-0.8], [0.32,-1.21], [-0.27,-1.65], [-0.81,-2.09], [-1.41,-2.54]])
            self.turn = True
            self.orientation = 'inicioNorte'
                
        elif self.orientation == 'inicioNorte' and self.position.flatten()[0] == 0 and self.position.flatten()[1] == 3:
            self.curve = np.array([[0.21,2.39], [0.53,1.78], [0.83,1.15], [1.19,0.42], [1.7,-0.29], [2.05,-0.93], [2.5,-1.5]])
            self.turn = True
            self.orientation = 'inicioOeste'
                
        elif self.orientation == 'inicioOeste' and self.position.flatten()[0] == -3 and self.position.flatten()[1] == 0:
            self.curve = np.array([[-2.38,0.24], [-1.74,0.5], [-1.01,0.8], [-0.32,1.21], [0.27,1.65], [0.81,2.09], [1.41,2.54]])
            self.turn = True
            self.orientation = 'inicioSur'
                
        elif self.orientation == 'inicioSur' and self.position.flatten()[0] == 0 and self.position.flatten()[1] == -3:
            self.curve = np.array([[-0.21,-2.39], [-0.53,-1.78], [-0.83,-1.15], [-1.19,-0.42], [-1.7,0.29], [-2.05,0.93], [-2.5,1.5]])
            self.turn = True
            self.orientation = 'inicioEste'

# Regresa las luces de los semáforos en un array
def arrLuces(model):
    res = []
    
    for agent in model.lights.agents:
        res.append(agent.light)
    
    res = np.asarray(res)
    return res

# Regresa los carros en un array
def arrCarros(model):
    res = []
    
    for agent in model.schedule.agents:
        res.append(agent.position)
    
    res = np.asarray(res)
    return res

class CarreteraModel(Model):
    def __init__(self, N):
        self.num_agents = N
        
        # Inicia los agentes
        self.schedule = RandomActivation(self)
        self.lights = RandomActivation(self)
        
        # Configura la caja de control
        self.inicioSem()
        self.control = CajaControl(1, self)
        
        self.id = 8
        
        # Posiciones iniciales donde pueden ir los carros
        self.source = np.array([[10, 0], [10, 2], [0, 10], [-2, 10], [-10, 0], [-10, -2], [0, -10], [2, -10]])
        
        temp = []
        i = 0
        
        # Asigna los carros
        g = np.random.randint(8)
        while i in range(g):
            pos = np.random.randint(8)
            
            if pos in temp:
                continue
            
            x = self.source[pos][0]
            y = self.source[pos][1]
            orientation = self.dirInicio(pos)
            car = Carro(i, self, x, y, orientation)
            self.schedule.add(car)
            temp.append(pos)
            i += 1

            
        self.datacollector = DataCollector(model_reporters = {"Carros" : arrCarros, "Luces" : arrLuces})

    def step(self):
        if self.id < self.num_agents:
            pos = np.random.randint(8)
            x = self.source[pos][0]
            y = self.source[pos][1]
            orientation = self.dirInicio(pos)
            car = Carro(self.id, self, x, y, orientation)
            self.schedule.add(car)
            self.id += 1
        
        self.datacollector.collect(self)
        self.schedule.step()
        self.control.step()
        
    
    # Define los semáforos que se utilizarán
    def inicioSem(self):
        self.semNorte = Semaforo(1, self)
        self.lights.add(self.semNorte)
        
        self.semSur = Semaforo(2, self)
        self.lights.add(self.semSur)
        
        self.semEste = Semaforo(3, self)
        self.lights.add(self.semEste)
        
        self.semOeste = Semaforo(4, self)
        self.lights.add(self.semOeste)        
    
    # Marca de donde iniciaron los carros
    def dirInicio(self, pos):
        if 0 <= pos <= 1:
            return 'inicioEste'
        
        elif 2 <= pos <= 3:
            return 'inicioNorte'
        
        elif 4 <= pos <= 5:
            return 'inicioOeste'
        
        elif 6 <= pos <= 7:
            return 'inicioSur'