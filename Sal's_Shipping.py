def ground_cost (weight):
  if weight <=2:
    ground_cost = weight*1.5+20
  elif weight <=6:
    ground_cost = weight*3+20
  elif weight <=10:
    ground_cost = weight*4+20
  else:
    ground_cost = weight*4.75+20
  return ground_cost

premium_cost = 125
	
def drone_cost (weight):
  if weight <=2:
    drone_cost = weight*4.5
  elif weight <=6:
    drone_cost = weight*9
  elif weight <=10:
    drone_cost = weight*12
  else:
    drone_cost = weight*14.25
  return drone_cost

def cheapest_shipping (weight):
 
  if ground_cost(weight) < premium_cost and ground_cost(weight) < drone_cost (weight):
    return "The most optimal is ground shipping method and will cost $ " + str(ground_cost (weight))
  elif  premium_cost < ground_cost (weight) and premium_cost < drone_cost (weight):
    return "The most optimal is premium shipping method and will cost $ " + str(premium_cost)
  else:
    return "The most optimal is drone shipping method and will cost $ " + str(drone_cost (weight))
         
print(cheapest_shipping(21.8))

 
