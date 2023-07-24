# Our football team has finished the championship.

# Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

# For example: ["3:1", "2:2", "0:1", ...]

# Points are awarded for each match as follows:

# if x > y: 3 points (win)
# if x < y: 0 points (loss)
# if x = y: 1 point (tie)
# We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

# Notes:

# our team always plays 10 matches in the championship


def solution(matches):
    # Season Total
    points = 0
    # Loop through each match
    for result in matches:
        # Get the score for each team - colon splits the scores 'x:y'
        scores = result.split(':')
        # team x is the first value in the list
        team_x = int(scores[0])
        # team y is the second value in the list
        team_y = int(scores[1])
        # if team x has more goals
        if team_x > team_y:
            # Team x wins, add 3 points to season total
            points += 3
        # if team y has more goals
        elif team_x < team_y:
            # Team x loses, no points to season total
            points += 0
        # if neither team x nor team y have more goals
        else:
            # Draw - add 1 point to season total
            points += 1
    # Once we've gone through all of the matches, return the season total points
    return points
    
