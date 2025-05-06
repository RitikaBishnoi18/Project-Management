from pymongo import MongoClient
from datetime import datetime
import random
from random import randint

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.projectManagement

# Create collections
clients = db.clients
employees = db.employees
projects = db.projects
statuses = db.statuses
tasks = db.tasks
sprints = db.sprints
audit_logs = db.auditLogs

clients_data = [
    {"_id": 1, "client_name": "Tech Solutions", "client_type": "Software"},
    {"_id": 2, "client_name": "HealthCare Ltd.", "client_type": "Healthcare"},
    {"_id": 3, "client_name": "Green Energy", "client_type": "Energy"}
]
clients.insert_many(clients_data)
# Insert dummy data for employees
employees_data = [
    {"_id": 101, "employee_name": "Alice","gender":"female", "role": "Developer"},
    {"_id": 102, "employee_name": "Bob", "gender":"male","role": "Manager"},
    {"_id": 103, "employee_name": "Charlie","gender":"male", "role": "Developer"},
    {"_id": 104, "employee_name": "David", "gender":"male","role": "Tester"},
    {"_id": 105, "employee_name": "Eve","gender":"female", "role": "Developer"},
    {"_id": 106, "employee_name": "Ritika","gender":"female", "role": "Manager"},
    {"_id": 107, "employee_name": "Umang", "gender":"male","role": "Developer"},
    {"_id": 108, "employee_name": "Shreya", "gender":"female","role": "Designer"}
]
employees.insert_many(employees_data)

statuses_data = [
    {"_id": 1, "status_name": "In Progress"},
    {"_id": 2, "status_name": "Completed"},
    {"_id": 3, "status_name": "On Hold"},
    {"_id": 4, "status_name": "Cancelled"}
]
statuses.insert_many(statuses_data)

# Insert dummy data for sprints
sprints_data = [
    {"_id": 1, "goal": "Develop Homepage", "start_date": datetime(2025, 5, 1),"end_date":None, "tentative_end_date": datetime(2025, 5, 15)},
    {"_id": 2, "goal": "Create User Authentication", "start_date": datetime(2025, 5, 16), "end_date":None,"tentative_end_date": datetime(2025, 5, 30)},
    {"_id": 3, "goal": "Develop Homepage", "project_id":3,"start_date": datetime(2025, 4, 1), "end_date":None,"tentative_end_date": datetime(2025, 7, 1)},
    {"_id": 4, "goal": "Develop Dashboard", "project_id":3,"start_date": datetime(2025, 7, 2), "end_date":None,"tentative_end_date": datetime(2025, 10, 1)}
]
sprints.insert_many(sprints_data)

# Insert dummy data for projects
projects_data = [
        {
        "_id": 1,
        "project_name": "Website Redesign",
        "client_id": 1,  # Foreign Key from clients collection
        "employee_ids": [101, 103, 105],  # Foreign Key from employees collection
        "manager_id": 102,  # Foreign Key from employees collection (Manager)
        "start_date": datetime(2025, 4, 1),
        "end_date": datetime(2025, 6, 1),
        "tentative_end_date":datetime(2025, 10, 1),
        "status_id": 1  # Foreign Key from statuses collection
    },
    {
        "_id": 2,
        "project_name": "Mobile App Development",
        "client_id": 2,  # Foreign Key from clients collection
        "employee_ids": [101, 103, 104],  # Foreign Key from employees collection
        "manager_id": 102,  # Foreign Key from employees collection (Manager)
        "start_date": datetime(2025, 3, 1),
        "end_date": None,
        "tentative_end_date":datetime(2025, 10, 1),
        "status_id": 2  # Foreign Key from statuses collection
    },
    {
        "_id": 3,
        "project_name": "Web App Development",
        "client_id": 2, 
        "employee_ids": [107, 108],  # Foreign Key from employees collection
        "manager_id": 106,  # Foreign Key from employees collection (Manager)
        "start_date": datetime(2025, 4, 1),
        "end_date": None,
        "tentative_end_date":datetime(2025, 10, 1),
        "status_id": 1  # Foreign Key from statuses collection
    }
]
projects.insert_many(projects_data)

# Insert dummy data for tasks
tasks_data = [
    {
        "_id": 1,
        "task_name": "Design Homepage",
        "project_id": 1,  # Foreign Key from projects collection
        "sprint_id": 1,  # Foreign Key from sprints collection
        "employee_id":101,
        "description": "Design the homepage layout for the website.",
        "status": "In Progress",
        "start_time": datetime(2025, 4, 2),
        "end_time": None,
        "tentative_end_time":datetime(2025, 5, 15)
    },
    {
        "_id": 2,
        "task_name": "Build Authentication API",
        "project_id": 2,  # Foreign Key from projects collection
        "sprint_id": 2,  # Foreign Key from sprints collection
        "employee_id":103,
        "description": "Create the backend API for user authentication.",
        "status": "Completed",
        "start_time": datetime(2025, 3, 5),
        "end_time": None,
        "tentative_end_time":datetime(2025, 5, 15)
    },
    {
        "_id": 3,
        "task_name": "Design Homepage",
        "project_id": 3,  # Foreign Key from projects collection
        "sprint_id": 3,  # Foreign Key from sprints collection
        "description": "Design the homepage layout for the website.",
        "status_id": 2,
        "employee_id":108,
        "start_time": datetime(2025, 4, 2),
        "end_time": None,
        "tentative_end_time":datetime(2025, 5, 15)
    },
    {
        "_id": 4,
        "task_name": "Develop Homepage",
        "project_id": 3,  # Foreign Key from projects collection
        "sprint_id": 3,  # Foreign Key from sprints collection
        "description": "Create the backend API for Home Page.",
        "status_id": 1,
        "employee_id":107,
        "start_time": datetime(2025, 5, 18),
        "end_time": None,
        "tentative_end_time":datetime(2025, 6, 27)
    }
]
tasks.insert_many(tasks_data)

audit_logs_data = [
    {
        "task_id": 1,  # Foreign Key from tasks collection
        "status_change": {
            "from_status": 1,  # "In Progress" (status_id = 1)
            "to_status": 2     # "Completed" (status_id = 2)
        },
        "employee_id": 102,  # Foreign Key from employees collection
        "changed_on": datetime(2025, 4, 4)
    },
    {
        "task_id": 2,  # Foreign Key from tasks collection
        "status_change": {
            "from_status": 2,  # "Completed" (status_id = 2)
            "to_status": 3     # "On Hold" (status_id = 3)
        },
        "employee_id": 104,  # Foreign Key from employees collection
        "changed_on": datetime(2025, 3, 20)
    }
]
audit_logs.insert_many(audit_logs_data)

print("Done")

task_groups = [
    [(1, "Design Footer", 1, 105, 102),
     (1, "Test Homepage", 2, 104, 102),
     (1, "Code Contact Page", 1, 101, 102)],

    [(2, "Build Notification Module", 1, 101, 102),
     (2, "Integrate Payment API", 2, 104, 102),
     (2, "Create Admin Dashboard", 1, 105, 102)],

    [(2, "UI Polish", 2, 103, 102),
     (2, "Optimize Images", 1, 103, 102),
     (2, "Setup CI/CD Pipeline", 2, 101, 102)],

    [(3, "Design Sidebar", 1, 108, 106),
     (3, "Setup MongoDB", 2, 107, 106),
     (3, "Build Chat Component", 1, 108, 106)],

    [(3, "Create User Profile Page", 2, 107, 106),
     (3, "Write Unit Tests", 1, 108, 106),
     (3, "Bug Fixes", 2, 107, 106)],
]

task_id = 5
sprint_id = 5
base_date = datetime(2025, 4, 10)
task_duration = timedelta(days=10)
sprint_duration = timedelta(days=20)

all_sprints = []
all_tasks = []

for group_index, group in enumerate(task_groups):
    project_id = group[0][0]
    sprint_start = base_date + timedelta(days=group_index * 4)
    sprint_tentative_end = sprint_start + sprint_duration
    sprint_delays = []

    # Sprint creation placeholder
    sprint_doc = {
        "_id": sprint_id,
        "goal": f"Sprint {sprint_id} deliverables",
        "project_id": project_id,
        "start_date": sprint_start,
        "tentative_end_date": sprint_tentative_end,
        "end_date": None  # To be filled later
    }

    for proj_id, task_name, status_id, employee_id, manager_id in group:
        task_start = sprint_start + timedelta(days=1)
        task_tentative_end = task_start + task_duration
        delay_days = random.randint(1, 5) if status_id == 2 else 0
        task_end = task_tentative_end + timedelta(days=delay_days) if status_id == 2 else None

        if task_end:
            sprint_delays.append((task_end - sprint_tentative_end).days)

        task_doc = {
            "_id": task_id,
            "task_name": task_name,
            "project_id": proj_id,
            "sprint_id": sprint_id,
            "employee_id": employee_id,
            "description": f"{task_name} for project {proj_id}",
            "status_id": status_id,
            "start_time": task_start,
            "tentative_end_time": task_tentative_end,
            "end_time": task_end
        }
        all_tasks.append(task_doc)
        task_id += 1

    # Sprint delay if any task delayed
    if sprint_delays:
        max_delay = max(0, max(sprint_delays))
        sprint_doc["end_date"] = sprint_tentative_end + timedelta(days=max_delay)
    else:
        sprint_doc["end_date"] = None

    all_sprints.append(sprint_doc)
    sprint_id += 1

# Insert into MongoDB
sprints.insert_many(all_sprints)
tasks.insert_many(all_tasks)

print("Inserted sprints and tasks with some delays in end dates.")
