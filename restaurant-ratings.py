def rest_ratings ():
    """
    Takes a file, then spits out the ratings in alphabetical order by restaurant.
    """

    input_file = open("scores.txt")
    restaurant_rating = {}

    for line in input_file:
        line = line.rstrip()
        rest_score = line.split(':')
        rest_name = rest_score[0]
        score = int(rest_score[1])
        restaurant_rating[rest_name] = score
    
    for rest_name, score in sorted(restaurant_rating.items()):
        print "%s is rated at %d" % (rest_name, score)

    input_file.close()