"""Student Score Analyzer
"""

def score_analyzer(scores):
    """Function that takes list of scores and prints
    highest, lowest, average scores and students that passed (>= 60)

    Args:
        scores (int[]): a list of scores in integers
    """
    max_score = max(scores)
    min_score = min(scores)
    avg_score = sum(scores) // len(scores)
    passed_students = [score for score in scores if score >= 60]
    print(f"Highest Score: {max_score}")
    print(f"Lowest Score: {min_score}")
    print(f"Average Score: {avg_score}")
    
    print(f"Students who passed ({len(passed_students)})")
    for score in passed_students:
        print(score)

scores = [45, 85, 74, 42, 87,
                  99, 61, 58, 33, 100]

score_analyzer(scores)