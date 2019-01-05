def create_cast_list(filename):
	cast_list = []

	with open(filename , 'r') as f:

		[cast_list.append(line.split(',')[0]) for line in f]

	return(cast_list)

filename = 'flying_circus_cast.txt'
actors_names = create_cast_list(filename) 

for actor in actors_names:
	print(actor) 

# def create_cast_list(filename):
#     cast_list = []
#     #use with to open the file filename
#     #use the for loop syntax to process each line
#     #and add the actor name to cast_list

#     cast_list = []
#     with open(filename, 'r') as f:
#         for line in f:
#             actors = line.split(",")[0]
#             cast_list.append(actors)
#     return cast_list

# cast_list = create_cast_list('flying_circus_cast.txt')
# for actor in cast_list:
#     print(actor)
	