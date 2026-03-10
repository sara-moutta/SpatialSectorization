from src.sectorization_algorithm import run_sectorization

#For a scenario with 20 neighborhoods
from data.scenario_20_districts import V, A, C

#For a scenario with 30 neighborhoods
#from data.scenario_30_districts import V, A, C 


run_sectorization(V, A, C)
