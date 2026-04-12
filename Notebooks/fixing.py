# Step 1 - create the cleaning script
with open("Notebooks\Feature_Engineering.ipynb", "r", encoding="utf-8") as f:
    
    lines = f.readlines()

cleaned = []
skip = False

for line in lines:
    if line.startswith("<<<<<<< HEAD"):
        skip = False
    elif line.startswith("======="):
        skip = True
    elif line.startswith(">>>>>>> "):
        skip = False
    else:
        if not skip:
            cleaned.append(line)

with open("model_training_fe.ipynb", "w", encoding="utf-8") as f:
    f.writelines(cleaned)

print("Done!")
