import pandas as pd
import json
from sklearn.model_selection import train_test_split


with open("./data/labeled_data.json") as file:
    data = json.load(file)

# merge title and description, separated by tokens
new_data=[]
for i in range(len(data)):
    # print(data[i]["number"], data[i]["labels"])
    if ((-1) not in data[i]["labels"]):
        data[i]["text"] = "[TITLE] "+ data[i]["title"] + " [DESC] " + data[i]["description"]
        new_data.append(data[i])

train, val = train_test_split(new_data, test_size=0.15, random_state=1, shuffle=True)

print("number of training: ", len(train))
print("number of validation: ", len(val))

train_df = pd.json_normalize(train)
train_df.to_csv("./data/training_data.csv", index=True)

val_df = pd.json_normalize(val)
val_df.to_csv("./data/validation_data.csv", index=True)