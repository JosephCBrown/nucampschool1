state_captials = {"Washington": "Olympia",
                  "Oregon": "Salem", "California": "Sacramento"}
"""
for state in state_captials:
    print(state)
"""
''''
for city in state_captials.values():
    print(city)
'''
'''
for state in state_captials:
    print(state_captials[state], "is the capital of", state)
'''
for state,city in state_captials.items():
    print(city, "is the capital of", state)