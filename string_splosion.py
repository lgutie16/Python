def string_splosion(str):
  sr = ""
  for i in range (len(str)):
    sr = sr + str[:i+1] 
  return sr