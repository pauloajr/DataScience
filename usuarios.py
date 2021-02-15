
users = [
        {"id":0, "nome": "Banha"},
        {"id":1, "nome":"Paulo Jr"},
        {"id":2, "nome":"Thiago"},
        {"id":3, "nome":"Julia"},
        {"id":4, "nome":"Roberta"},
        {"id":5, "nome":"Guadalupe"},
        {"id":6, "nome":"Leonardo"}
        ]

friendships = [ (2,4), (5,1), (2,6), (1,2), (1,3), (0,1)]


for user in users:
    user["friends"] = []


for i, j  in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])


def number_of_friends(user):
    return len(user["friends"])


"""
Ahora queremos saber cual es numero medio de las conexiones
"""

todas_las_conexiones = sum(number_of_friends(user) for user in users) # 10

num_users = len(users)

avg_conexiones = todas_las_conexiones / num_users

print(avg_conexiones)

# no hay muchas personas entonces podriamos sortea de muchos a pocos

""" vamos criar uma lista com id_users, numero de amigos """
num_friends_by_id = [
    (user["id"], number_of_friends(user)) for user in users
]


a = sorted(num_friends_by_id, 
      key=lambda t: t[1], 
      reverse=True)

print(a)


def friends_of_friend_ids_bad(user):
    return [foaf["id"]
            for friends in user["friends"]
            for foaf in friends["friends"]
        ]

print(friends_of_friend_ids_bad(users[0]))

from collections import Counter

def no_es_lo_mismo(user, other_user):
	return user["id"] != other_user["id"]
	
def no_amigos(user, other_user):
	return all(no_es_lo_mismo(friend, other_user)
				for friend in user["friends"])

def amigos_del_amigos_ids(user):
	return Counter(foaf["id"]
					for friends in user["friends"]
					for foaf in friends["friends"]
					if no_es_lo_mismo(user,foaf)
					and no_amigos(user,foaf))
					
print(amigos_del_amigos_ids(users[0]))

interests = [ (0,"Hadoop"), (0,"Big Data"), (6,"Big Data")
			]
			
def data_scientists_who_like(target_interest):
	return [user_id
			for user_id, user_interest in interests
			if user_interest == targe_interest]
			
from collections import defaultdict

# as chaves são interesses, os valores são listas de user_ids com interests
user_ids_by_interest = defaultdict(list)

for user_id, ainterests in interests:
	user_ids_by_interest[ainterests].append(user_id)
	
print(user_ids_by_interest)

# as chaves são user_ids, os valores são as listas de interests para aquele user_id
interests_by_user_id = defaultdict(list)

for user_id, ainterests in interests:
	interests_by_user_id[user_id].append(ainterests)

print(interests_by_user_id)

def con_los_mismo_interesses(user):
	return Counter(interessados_por_id
					for interest in interests_by_user_id[user["id"]]
					for interessados_por_id in user_ids_by_interest[interest]
					if interessados_por_id != user["id"])
					
print(con_los_mismo_interesses(users[0]))
