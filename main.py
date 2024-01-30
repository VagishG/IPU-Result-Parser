import camelot
import pandas as pd
for a in range(1,144):
    print(str(a))
    tables=camelot.read_pdf("rr.pdf", pages=str(a))
    table = tables[0].df
    for a in table.iloc[0]:
        if a=="CS/Remarks":
            index=table.iloc[0][3].find("Institution:")
            table_Name = f"{table.iloc[0][3][index+13:].replace(' ', '_')}.csv"
            table.to_csv(table_Name, mode='a', index=False)
            break           
        
# table.to_excel("resuslts.xlsx", index=False)

