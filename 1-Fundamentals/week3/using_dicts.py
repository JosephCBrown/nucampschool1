state_captials = {"Washington": "Olympia","Oregon": "Salem", "California": "Sacramento"}
#print(len(state_captials))
#print(state_captials["Washington"])
state_captials["Washington"] = "Aberdeen"
state_captials["Texas"] = "Austin"
print(state_captials)
del state_captials["California"]
print(state_captials)
removed_capital = state_captials.pop("Oregon")
print(state_captials)
print(removed_capital)