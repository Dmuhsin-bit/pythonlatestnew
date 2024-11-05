# '''Task: Write a Python function called track_scores
# Create a function that can take an arbitrary number of game scores as arguments.
# The function should print:
#
# The highest score.
# The lowest score.
# The total number of scores provided.
# If no scores are provided, it should print: "No scores to track."
# Call the function with the scores 45, 67, and 89.'''


def track_scores(*score):

    if not score:
        print("No scores to track..")
    else:
         highscore = max(score)
         lowscore = min(score)
         total = len(score)

         print(f"Maximum Score: {highscore}")
         print(f"Minimum score: {lowscore}")
         print(f"Total number of scores: {total}")

track_scores(1,3,4,2)
track_scores()

