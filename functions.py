import math
def small_to_large(numb):
    for n in range(0, len(numb)):
        for i in range(n+1, len(numb)):
            if numb[n] > numb[i]:
                numb[n], numb[i] = numb[i], numb [n]
    return numb


def large_to_small(numb):
    for n in range(0, len(numb)):
        for i in range(n+1, len(numb)):
            if numb[n] < numb[i]:
                numb[n], numb[i] = numb[i], numb [n]
    return numb


def list_ranking(task_rankings):
    return sorted(task_rankings, key=lambda x: x['ranking'], reverse=True)


def importance_ranking_algorithm():
    task_ranking = []
    while True:
        task_name = input("Enter a task (or 'end' to exit): ")
        if task_name.lower() == "end":
            break
        importance_ranking = int(input("1 / 10, how important is this task to you? "))
        if importance_ranking < 1 or importance_ranking > 10:
            raise ValueError("Please enter a number between 1 and 10.")
        importance_ranking /= 10
        days = int(input("How many days until this task is due? (Enter 0 for no due date): "))
        if days < 0:
            raise ValueError("Please enter a positive number or 0 for no due date.")
        elif days == 0:
            days = math.inf
        time_ranking = 0.5 * math.exp(-0.15 * (days - 1)) + 0.5
        final_ranking = (time_ranking + importance_ranking) / 2
        task_ranking.append({"task": task_name, "ranking": final_ranking})
    sorted_task_rankings = list_ranking(task_ranking)
    for item in sorted_task_rankings:
        print(f"Task: {item['task']}, Ranking: {item['ranking']:.2f}")