# %%
from pymongo import MongoClient
from datetime import datetime
from random import randint
client = MongoClient('mongodb://localhost:27017/')

# %%
import pandas as pd
db = client['projectManagement']
collection=db['projects']

start_cutoff=datetime(2025,3,1)

query={
    'start_date':{
        '$gt':start_cutoff
    }
}

project={
    'project_id':'$_id'
}

result_data=collection.find(query,project)
df_project=pd.DataFrame(list(result_data))
df_project=df_project.drop(columns='_id')
df_project

project_list=tuple(df_project['project_id'].tolist())

# %%
db = client['projectManagement']
collection=db['tasks']

query={
    'project_id' : {
        '$in':project_list
    }
}

result_data=collection.find(query)
df_tasks=pd.DataFrame(list(result_data))
df_tasks=df_tasks.rename(columns={'_id':'task_id'})
df_tasks=df_tasks.drop(columns='description')
df_tasks


# %%
df_tasks['end_time'] = df_tasks['end_time'].astype(str).replace('NaT', '')
df_tasks

# %%
projects_list=tuple(df_tasks['project_id'].tolist())
sprint_list=tuple(df_tasks['sprint_id'].tolist())
employee_list=tuple(df_tasks['employee_id'].tolist())

# %%
import pandas as pd
db = client['projectManagement']
collection=db['projects']

pipeline=[
    {'$match':{
            '_id':{
                '$in':projects_list
            }
        }
    },
    {
        '$lookup':{
            'from':'clients',
            'localField':'client_id',
            'foreignField':'_id',
            'as':'client_info'
        }
    },
    {
        '$unwind':'$client_info'
    },
    {
        '$project': {
            '_id': 0,
            'project_id': '$_id',
            'project_name': 1,
            'client_id': 1,
            'client_name':'$client_info.client_name',
            'manager_id':1,
            'start_date':1,
            'end_date':1,
            'tentative_end_date':1
        }
    }
]
result_data=collection.aggregate(pipeline)
df_projects_info=pd.DataFrame(list(result_data))
df_projects_info=df_projects_info[['project_id','project_name','client_id',
                                   'client_name','manager_id','start_date','end_date','tentative_end_date']]
df_projects_info


# %%
manager_list=tuple(df_projects_info['manager_id'].tolist())

import pandas as pd
db = client['projectManagement']
collection=db['employees']

pipeline=[
    {'$match':{
            '_id':{
                '$in':employee_list
            }
        }
    },
    {
        '$project': {
            '_id': 0,
            'manager_id': '$_id',
            'name': '$employee_name',
            'gender':1
        }
    }
]
result_data=collection.aggregate(pipeline)
df_manager_info=pd.DataFrame(list(result_data))
df_manager_info=df_manager_info[['manager_id','name','gender']]
df_manager_info


# %%
import pandas as pd
db = client['projectManagement']
collection=db['sprints']

pipeline=[
    {'$match':{
            '_id':{
                '$in':sprint_list
            }
        }
    },
    {
        '$project': {
            '_id': 0,
            'sprint_id': '$_id',
            'sprint_name': '$goal',
            'start_date':1,
            'end_date':1,
            'tentative_end_date':1
        }
    }
]
result_data=collection.aggregate(pipeline)
df_sprint_info=pd.DataFrame(list(result_data))
df_sprint_info=df_sprint_info[['sprint_id','sprint_name','start_date','end_date','tentative_end_date']]
df_sprint_info


# %%
import pandas as pd
db = client['projectManagement']
collection=db['employees']

pipeline=[
    {'$match':{
            '_id':{
                '$in':employee_list
            }
        }
    },
    {
        '$project': {
            '_id': 0,
            'employee_id': '$_id',
            'name': '$employee_name',
            'gender':1
        }
    }
]
result_data=collection.aggregate(pipeline)
df_employee_info=pd.DataFrame(list(result_data))
df_employee_info=df_employee_info[['employee_id','name','gender']]
df_employee_info


# %%
import pandas as pd
db = client['projectManagement']
collection=db['statuses']

result_data=collection.find()
df_status_info=pd.DataFrame(list(result_data))
df_status_info



