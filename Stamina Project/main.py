
import pandas as pd
import functions as fun

data = {
    "CharacterName": ["Geralt of Rivia", "Jaskier aka Dandelion", "Ciri the Princess", "Yennefer the Witch"],
    "Terrain": ["Foragers Forest", "Mystical Mountain", "Savage Swamp", "Treacherous Tundra"],
    "Stamina": [100, 100, 100, 100]  # Assuming each character starts with 100 stamina
}
df = pd.DataFrame(data)

df["Stamina Adjustment"] = df["Terrain"].apply(fun.stamina_adjustment) #applies and "saves" stamina adjustment to stamina adjustment column
df["Stamina"] = df["Stamina"] + df["Stamina Adjustment"] #adjusts actual stamina column



#prints the results
print(df)