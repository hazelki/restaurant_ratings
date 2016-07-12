def rest_ratings ():
    """
    Takes a file, then spits out the ratings in alphabetical order by restaurant.
    """

    input_file = open("scores.txt")
    restaurant_rating = {}

    for line in input_file:
        line = line.rstrip()
        rest_name, score = line.split(":")
        restaurant_rating[rest_name] = int(score)
    
    for rest_name, score in sorted(restaurant_rating.items()):
        print "%s is rated at %d" % (rest_name, score)

    input_file.close()

rest_ratings()
