# data types and variables exercises

movies = {'name': 'the little mermaid', 'days_rented': 3}, {'name': 'brother bear', 'days_rented': 5}, {'name': 'hercules', 'days_rented': 1}

print(movies)

[cost['days_rented'] * 3 for cost in movies]




contract = [['google', 400], ['amazon', 380], ['facebook', 350]]

print(contract)

print(contract[0][1] * 6, contract[1][1] * 4, contract[2][1] * 10)




class_is_not_full = True
class_does_not_conflict = True
class_is_full = False
class_does_conflict = False

class_is_not_full and class_does_not_conflict 
class_is_not_full and class_does_conflict
class_is_full and class_does_conflict
class_is_full and class_does_not_conflict




regular_one_item = False
regular_two_items = True
premium_one_item = True
offer_not_expired = True
offer_expired = False

regular_one_item and offer_not_expired
regular_two_items and offer_not_expired
premium_one_item and offer_not_expired
premium_one_item and offer_expired




username = 'codeup'
password = 'notastrongpassword'

len(password) >= 5
len(username) <= 20
password != username
password == password.strip()
username == username.strip()


