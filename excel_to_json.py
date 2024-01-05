import pandas as pd
import yaml
# xls = pd.ExcelFile('Data Taxonomy_client.xlsx')
xls=pd.ExcelFile('Data Taxonomy_workforce.xlsx')
sheet_name=xls.sheet_names
print(sheet_name)
# "Client core details","Client Investment Details" ,"Account"
# sheet_name_client=["Client core details" ,"Account","L0"]
sheet_name=["Client servicing Employee","Client Supporting Employee","Users","L0"]
sheet_name.remove('L0')
df_L0 = pd.read_excel(xls, 'LO ')
df_L0_cp=df_L0.copy()
# df_json=df.to_dict(orient='index')
# df_js={}
# df_js["nodes"]=df_json

final_json={}
L0_list=[]
for sheet in sheet_name:
    print(sheet)
    L1_dic={}
    L0_dic={}
    L1_list=[]
    L2_list=[]
    L0_dic["name"]=str(df_L0[df_L0["L1"].str.strip()==str(sheet)]["LO "].tolist()[0])
    L0_dic["description"]=str(df_L0[df_L0["L1"].str.strip()==str(sheet)]["Definition"].tolist()[0])
    L1_dic["name"]=str(df_L0_cp[df_L0_cp["L1"].str.strip()==str(sheet)].L1.tolist()[0])
    L1_dic["description"]=str(df_L0_cp[df_L0_cp["L1"].str.strip()==str(sheet)]["Definition.1"].tolist()[0])
    print(L1_dic,L0_dic)
    df=pd.read_excel(xls,sheet)
    distinct_v=df["L2"].unique().tolist()
    for i in distinct_v:
        if(str(i)=='nan'):
            continue

        L2_dic={}
        L2_dic["name"]=str(i)
        L2_dic["description"]=str(df[df.L2.isin([i])].Definition.tolist()[0])
        L2_dic["owners"]= {"users": ["datahub"]}
        new_df=df[df.L2.isin([i])]
        new_ds=new_df["L3"].unique().tolist()
        L3_list=[]
        for j in new_ds:
            terms_node=[]
            if(str(j) =='nan'):
                print("continue")
                continue
            L3_dic={}
            
            L3_dic["name"]=str(j)
            L3_dic["description"]=str(new_df[new_df.L3.isin([j])].Definition.tolist()[0])
            L3_dic["owners"]= {"users": ["datahub"]}
            new_df1=new_df[new_df.L3.isin([j])]
            term_list=new_df1.L4.unique().tolist()
            # print(term_list)
            for term in term_list:
                if(str(term)=='nan'):
                    continue
                term_dic={}
                
                term_dic["name"]=str(term)
                term_dic["description"]= str(new_df[new_df.L4.isin([term])].Definition.tolist()[0])
                term_dic["owners"]= {"users": ["datahub"]}
                terms_node.append(term_dic)
            L3_dic["terms"]=terms_node
            L3_list.append(L3_dic)
        L2_dic["nodes"]=L3_list
        
        L2_list.append(L2_dic)

    L1_dic["nodes"]=L2_list
    L1_list.append(L1_dic)
    L0_dic["nodes"]=L1_list
    L0_list.append(L0_dic)


    final_json["version"]= 1
    final_json["source"]="DataHub"
    final_json["owners"]= {"users": ["datahub"]}
    final_json["url"]="https://github.com/datahub-project/datahub/"
    final_json["nodes"]=L0_list




# print(final_json)
# ymal_string=yaml.dump(final_json, sort_keys=False)
# print("The YAML string is:")\
# print(ymal_string)
with open('business_gls_workforce.yml', 'w') as outfile:
    yaml.dump(final_json, outfile, sort_keys=False, default_flow_style=False)
   
