from bm_api_dev.User import User
from bm_api_dev.Project import Project

user = User()
user.login()

project_id = ""
project = Project(project_id, user)
