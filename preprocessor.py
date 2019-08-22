import pandas as pd
import numpy as np

df_raw_train_transaction=pd.read_csv('train_transaction.csv')
#df_raw_train_identity=pd.read_csv('train_identity.csv')
for x in df_raw_train_transaction.columns:
	print(x,df_raw_train_transaction[x].dtype)

strings=['ProductCD','P_emaildomain','R_emaildomain','card1','card2','card3','card4','card5','card6','addr1','addr2']
for x in strings:
	df_raw_train_transaction[x]=df_raw_train_transaction[x].astype(str)

joiner=['card1','card2','card3','card4','card5','card6']
df_raw_train_transaction['card']=df_raw_train_transaction[joiner].apply(lambda x: '-'.join(x),axis=1)

print(df_raw_train_transaction['card'].head())

dropcols=['TransactionDT','card1','card2','card3','card4','card5','card6']
df_raw_train_transaction=df_raw_train_transaction.drop(columns=dropcols)

for x in df_raw_train_transaction.columns:
	print(x,df_raw_train_transaction[x].dtype)
