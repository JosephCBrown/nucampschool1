states = ["Washington", "Oregon", "California"]
"""
print(states[0])
print(states[1])
print(states[2])
print(states[-1])
print(states[-2])
print(states[-3])
"""

states[2] = "Arizona"
# print(states)
# print(len(states))

states.append("New York") #adds to the end of the list
print(states)
states.pop() #removes a lsit item
print(states)
states.pop(1) #removes the item from the list at index 1
print(states)