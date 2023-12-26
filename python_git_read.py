import pandas as pd
import requests
import yaml
#import io
#from io import StringIO
#from git import Repo
#username= 'puneet664'
#token = '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'
#github_session = requests.Session()
#github_session.auth = (username, token)

# url = 'https://github.com/puneet664/test_dbt_qw/blob/main/data_test.csv'
#url='https://raw.githubusercontent.com/puneet664/test_dbt_qw/main/data_test.csv'
#export = requests.get(url,verify=False).text
#df = pd.read_excel(io.StringIO(export))
xls=pd.ExcelFile('Data Taxonomy_workforce.xlsx')
df = pd.read_excel(xls, 'LO ')
# Convert DataFrame to CSV in memory
#csv_buffer = StringIO()
#df.to_csv(csv_buffer, index=False)
#csv_content = csv_buffer.getvalue()
final_json = df.to_json(orient='records')[1:-1].replace('},{', '} {')
with open('business_glossary_code_workforce.yaml', 'w') as outfile:
    yaml.dump(final_json, outfile, sort_keys=False, default_flow_style=False)
   
