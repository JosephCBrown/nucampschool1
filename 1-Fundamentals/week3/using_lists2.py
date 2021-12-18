states = ["Washington", "Oregon", "California"]

'''for state in states: #instead of x made variable more descriptive
    state = state.lower() #made all the variables lower case
    print(state)
'''
''''
print("Washington" in states)
print("Tennessee" in states)
print("Washington" not in states)
'''

states2 = ["Arizona", "Ohio", "Louisiana"]
best_states = states + states2
print(best_states)

# slicing a list
# specifiy where to slice from in the index to where to end
print(best_states[1:3])
print(best_states[:2])  # slice the index from the start of list up index 2
print(best_states[4:])  # slice the index from index 4 to the end of the index
