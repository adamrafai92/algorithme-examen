import time
import datetime

# Réservoir pour stocker l'huile
tank = 0
# Stocks pour stocker les articles produits
wheels = 0
motors = 0

# Capacité maximale de stockage du réservoir
MAX_CAPACITY = 100

# Période et temps d'exécution pour chaque pompe
pump1_period = 2
pump1_execution_time = 3

pump2_period = 5
pump2_execution_time = 4

# Huile requise par chaque machine pour produire un article
machine1_oil = 10
machine2_oil = 15

def pump1():
    global tank
    # Vérifiez s'il y a suffisamment d'espace dans le réservoir pour stocker l'huile extraite.
    if tank + pump1_execution_time <= MAX_CAPACITY:
        tank += pump1_execution_time
        print("Pump 1: Extraction {} unités huile et ajout au reservoir. Current tank: {}".format(pump1_execution_time, tank))
    else:
        print("Pump 1: Impossible extraction huile car le réservoir est plein.")

def pump2():
    global tank
    #  Vérifiez s'il y a suffisamment d'espace dans le réservoir pour stocker l'huile extraite.
    if tank + pump2_execution_time <= MAX_CAPACITY:
        tank += pump2_execution_time
        print("Pump 2: Extraction {} unités huile et ajout au reservoir. Current tank: {}".format(pump2_execution_time, tank))
    else:
        print("Pump 2: Impossible extraction huile car le réservoir est plein.")

def machine1():
    global tank, wheels
    # Vérifiez s'il y a assez d'huile pour faire fonctionner la machine.
    if tank >= machine1_oil:
        tank -= machine1_oil
        wheels += 1
        print("Machine 1: Produced 1 wheel. Current wheels: {}".format(wheels))
    else:
        print("Machine 1: Not enough oil to produce a wheel.")

def machine2():
    global tank, motors
    # Vérifiez s'il y a assez d'huile pour faire fonctionner la machine.
    if tank >= machine2_oil:
        tank -= machine2_oil
        motors += 1
        print("Machine 2: Produced 1 motor. Current motors: {}".format(motors))
    else:
        print("Machine 2: Not enough oil to produce a motor.")

def scheduler():
    global tank, wheels, motors
    task_list = [pump1, pump2, machine1, machine2]

    for task in task_list:
        # Si le réservoir est plein les pompes doivent avoir une faible priorité
        if task in [pump1, pump2] and tank == MAX_CAPACITY:
            continue
        # Inverssmeent 
        elif task == machine1 and wheels / 4 > motors:
            task()
      
        elif task == machine2 and wheels / 4 < motors:
            task()
        # 
        else:
            task()

def simulation():
    start_time = datetime.datetime.now().minute
    while (data)
    
    
if __name__ == "__main__":
    scheduler()
    
