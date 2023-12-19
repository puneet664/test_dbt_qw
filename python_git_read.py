import pandas as pd
import requests
import io
username= 'puneet664'
token = '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'
github_session = requests.Session()
github_session.auth = (username, token)

# url = 'https://github.com/puneet664/test_dbt_qw/blob/main/data_test.csv'
url='https://raw.githubusercontent.com/puneet664/test_dbt_qw/main/data_test.csv'
export = requests.get(url,verify=False).text
df = pd.read_csv(io.StringIO(export))