def main(arr):
    scores = list(arr)
    sorted_scores = sorted(scores, reverse=True)
    ascending_scores = sorted(scores)
    best_score = sorted_scores[0]

    for score in ascending_scores:
        if score != best_score:
            runner_up_score = score

    return runner_up_score


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(main(arr))
