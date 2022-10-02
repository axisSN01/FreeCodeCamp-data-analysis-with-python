import numpy as np

def calculate(list):
  
  try:
    if len(list) != 9:
      raise ValueError("List must contain nine numbers.")
      
    calculations={
    'mean': [0, 0, 0],
    'variance': [0, 0, 0],
    'standard deviation': [0, 0, 0],
    'max': [0, 0, 0],
    'min': [0, 0, 0],
    'sum': [0, 0, 0]
    }
    functions=['mean','var','std','amax','min','sum']
    
    arr=np.array(list)
    mtx=np.array(list).reshape((3,3)).copy()
########################################
    for j,key in enumerate(calculations):
      i=functions[j]
      calculations[key]=eval(f'[np.{i}(mtx,axis=0).tolist(),np.{i}(mtx,axis=1).tolist(),np.{i}(arr).tolist()]')
    
    
    return calculations
  
  except:
    raise ValueError("List must contain nine numbers.")

