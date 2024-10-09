import csv
import pandas as pd


with open('database/urls_pos.txt', 'r') as document:
    sonuc_listesi = []
    
    for satir in document:
        baslangic = satir.find('tt0')
        bitis = satir.find('/', baslangic)
        
        
        if baslangic != -1 and bitis != -1:
            veri = satir[baslangic:bitis]
            sonuc_listesi.append(veri)
#set_sonuc = set(sonuc_listesi)           
#print(len(set_sonuc))

df = pd.read_csv("database/output.csv")
new_df = df[df.iloc[:, 0].isin(sonuc_listesi)]
#print(new_df)

with open('profiles1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["tconst"]
    writer.writerow(field)
    writer.writerow(sonuc_listesi)    
print(file)
    
    

csv_file = pd.read_csv("database/IMDB Dataset.csv")




