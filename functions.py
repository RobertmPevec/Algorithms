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
    elif ranking >= 0.9:
        return "Very High Priority"
    elif ranking >= 0.8:
        return "High Priority"
    elif ranking >= 0.65:
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


def importance_ranking_algorithm():
    summary_message = ""
    task_rankings = []
    today = datetime.now().date()
    while True:
        task_name = input("Enter a task (or 'end' to exit): ")
        if task_name.lower() == "end":
            break
        importance_ranking = float(input("On a scale of 1 to 10, how important is this task to you? "))
        if importance_ranking < 1 or importance_ranking > 10:
            print("Please enter a number between 1 and 10.")
            continue
        importance_ranking /= 10

        due_date_input = input("Enter the due date for this task (YYYY-MM-DD) or leave blank for no due date: ")
        if due_date_input:
            due_date = datetime.strptime(due_date_input, "%Y-%m-%d").date()
            days_until_due = (due_date - today).days
        else:
            days_until_due = math.inf

        if days_until_due != math.inf:
            time_ranking = 0.75 * math.exp(-0.3 * (days_until_due - 1)) + 0.25
        else:
            time_ranking = 0.25

        final_ranking = (time_ranking + importance_ranking) / 2
        task_rankings.append({"task": task_name, "ranking": final_ranking, "days_until_due": days_until_due})

    priority_groups = group_tasks_by_priority(list_ranking(task_rankings))
    for category, tasks in priority_groups.items():
        if tasks:
            summary_message += f"\n{category}:\n"
            for task in tasks:
                if task['days_until_due'] == math.inf:
                    due_date_str = "Due date N/A"
                elif task['days_until_due'] == 0:
                    due_date_str = ""
                elif task['days_until_due'] == 1:
                    due_date_str = ""
                elif task['days_until_due'] < 0:
                    due_date_str = f"{abs(task['days_until_due'])} days overdue"
                else:
                    due_date_str = f"Due in {task['days_until_due']} days"

                summary_message += f"{task['task']} | {due_date_str}\n"

    return summary_message

from functions import importance_ranking_algorithm
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import key
summary_message = importance_ranking_algorithm()
client = Client(key.account_sid, key.auth_token)
message = client.messages.create(
    body=summary_message,
    from_=key.twilio_number,
    to=key.target_number
)
print(message.body)

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Receive incoming messages without sending a message response."""
    resp = MessagingResponse()

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)

