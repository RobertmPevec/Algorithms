import math
from datetime import datetime


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


def categorize_ranking(ranking, days_until_due):
    if days_until_due < 0:
        return "Overdue"
    elif days_until_due == 0:
        return "Due Today"
    elif days_until_due == 1:
        return "Due Tomorrow"
    elif ranking >= 0.875:
        return "Very High Priority"
    elif ranking >= 0.75:
        return "High Priority"
    elif ranking >= 0.60:
        return "Medium Priority"
    elif ranking >= 0.35:
        return "Low Priority"
    else:
        return "Very Low Priority"


def group_tasks_by_priority(tasks):
    priority_groups = {"Overdue": [],"Due Today": [], "Due Tomorrow": [], "Very High Priority": [], "High Priority": [],
                       "Medium Priority": [], "Low Priority": [], "Very Low Priority": []}
    for task in tasks:
        category = categorize_ranking(task["ranking"], task["days_until_due"])
        priority_groups[category].append(task)
    return priority_groups


def importance_ranking_algorithm(tasks):
    summary_message = ""
    today = datetime.now().date()
    task_rankings = []
    summary_message += "Here is your updated task list:"
    for task in tasks:
        task_name = task["name"]
        due_date_input = task["due_date"]
        weight = task["weight"]

        importance_ranking = float(weight) / 10

        # Handle 'n/a' due dates
        if due_date_input.lower() == "n/a":
            days_until_due = math.inf
        else:
            due_date = datetime.strptime(due_date_input, "%Y-%m-%d").date()
            days_until_due = (due_date - today).days

        if days_until_due != math.inf:
            time_ranking = 0.70 * math.exp(-0.3 * (days_until_due - 1)) + 0.3
        else:
            time_ranking = 0.3

        final_ranking = (time_ranking + importance_ranking) / 2
        task_rankings.append({"task": task_name, "ranking": final_ranking, "days_until_due": days_until_due})

    priority_groups = group_tasks_by_priority(list_ranking(task_rankings))

    for category, tasks in priority_groups.items():
        if tasks:
            summary_message += f"\n{category}:\n"
            for task in tasks:
                due_date_str = "Due date N/A" if task['days_until_due'] == math.inf else f"Due in {task['days_until_due']} days"
                if task['days_until_due'] < 0:
                    due_date_str = f"{abs(task['days_until_due'])} days overdue"
                elif task['days_until_due'] == 0:
                    due_date_str = "Due Today"
                elif task['days_until_due'] == 1:
                    due_date_str = "Due Tomorrow"

                if task['days_until_due'] < 0 or task['days_until_due'] >= 2:
                    summary_message += f"-{task['task']} | {due_date_str}\n"
                else:
                    summary_message += f"-{task['task']}\n"

    return summary_message
