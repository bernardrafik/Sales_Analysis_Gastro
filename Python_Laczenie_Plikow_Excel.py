#!/usr/bin/env python
# coding: utf-8

#  ### Kod łączący wszystkie pierwotne pliki w jeden plik excel

# In[1]:


# C:\Users\Dell\Desktop\Nauka_DA\GitKraken\Gastro_Sales_Analysis
# Sciezka do plikow 

import os
import glob          
import pandas as pd 
files = glob.glob(r"C:\Users\Dell\Desktop\Nauka_DA\GitKraken\Gastro_Sales_Analysis\*.xlsx") 
                #znalezienie wszystkich plikow excel w folderze
  
                #przejecie dataframow
dfs = []        

                #petla - wczyta poprawnie pliki (pominie 2 wiersze informacyjne)
for file in files:            
    df=pd.read_excel(file, skiprows=2)  
    dfs.append(df)
    
merge_df = pd.concat(dfs, ignore_index=True)  #scalanie plików "jeden po drugim"

output_file = os.path.join(r"C:\Users\Dell\Desktop\Nauka_DA\GitKraken\Gastro_Sales_Analysis", "Sales_Report.xlsx")
merge_df.to_excel(output_file, index=False)

print(f"Zapisano Plik: {output_file}")


# ### Informacje o końcowym pliku

# In[2]:


import pandas as pd 

df = pd.read_excel(r"C:\Users\Dell\Desktop\Nauka_DA\GitKraken\Gastro_Sales_Analysis\Sales_Report.xlsx")
df.info()

