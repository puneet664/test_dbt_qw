import pandas as pd
import requests
import io
from git import Repo
username= 'puneet664'
token = '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'
github_session = requests.Session()
github_session.auth = (username, token)

# url = 'https://github.com/puneet664/test_dbt_qw/blob/main/data_test.csv'
url='https://raw.githubusercontent.com/puneet664/test_dbt_qw/main/data_test.csv'
export = requests.get(url,verify=False).text
df = pd.read_csv(io.StringIO(export))
# Convert DataFrame to CSV in memory
csv_buffer = StringIO()
df.to_csv(csv_buffer, index=False)
csv_content = csv_buffer.getvalue()
 
# Path to your local repository
repo_path = 'test_dbt_qw'  # Replace with your local repository path
 
# Commit message
commit_message = 'Add CSV file'
 
# File name for the CSV in the repository
file_name = 'data.csv'
 
# Open the Git repository
repo = Repo(repo_path)
 
# Write the CSV content to a file in the repository
with open(f'{repo_path}/{file_name}', 'w') as file:
    file.write(csv_content)
 
# Stage changes
repo.index.add([file_name])
 
# Commit changes
repo.index.commit(commit_message)
 
# Push changes to remote (optional)
origin = repo.remote(name='origin')  # Replace 'origin' with your remote name
origin.push()
# df.to_csv("file_name_git.csv")