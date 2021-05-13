def latest(scores):
    return scores[-1]


def highest_score(scores):
    return max(scores)


def top_three(scores):
    scores.sort(reverse=True)
    return scores[0:3]
 
def highest_to_lowest(scores):
    scores.sort(reverse=True)
    return scores

def only_two_results(scores):
    scores.sort(reverse=True)
    if len(scores) < 3:
        player_count = len(scores)

    return scores[0:player_count]


def only_one_result(scores):
    if len(scores) < 3:
        player_count = len(scores)
    return scores[0:player_count] #this lets the scores print for top 1 2 or 3 depending who played
    
    


