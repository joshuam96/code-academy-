weight = 4.8
#Ground Shipping 
if weight <= 2:
 cost_ground = weight * 1.5 + 20 
 print("Ground Shipping $",cost_ground)
elif weight <=6:
 cost_ground = weight * 3.00 + 20
 print("Ground Shipping $",cost_ground)
elif weight <=10:
 cost_ground = weight * 4.00 + 20 
 print("Ground Shipping $", cost_ground) 
else:
  cost_ground = weight * 4.75 + 20 
  print("Ground Shipping $", cost_ground)

#Premium 
ground_shipping_premium = 125.0
print("Ground Shipping Premium $",ground_shipping_premium)

#Drone Shipping 
if weight <= 2:
  cost_drone = weight * 4.50 + 0 
  print("Drone Shipping $",cost_drone)
elif weight <= 6:
  cost_drone = weight * 9.00 + 0 
  print("Drone Shippping $",cost_drone)
elif weight <=10:
    cost_drone = weight * 12 + 0 
    print("Drone Shipping $",cost_drone)
else:
    cost_drone = weight * 14.25 + 0 
    print("Drone Shipping $",cost_drone)








