import re
import os

goal_names = {
    1: "Green Gujarat : Plantation drives",
    2: "Anganwadi : ICDS",
    3: "Rural Development",
    4: "Women Empowerment",
    5: "Sanitation for all",
    6: "Water Projects",
    7: "Education Support",
    8: "Solar energy",
    9: "Nari Gruh",
    10: "Disabled / Elderly"
}

for i in range(1, 11):
    filename = f"goal-{i}.html"
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_h1 = f"<h1>Goal {i}: {goal_names[i]}</h1>"
        content = re.sub(rf"<h1>Goal {i}: .*?</h1>", new_h1, content)
        
        new_title = f"<title>GRGVS | Goal {i}: {goal_names[i]}</title>"
        content = re.sub(rf"<title>GRGVS \| Goal {i}: .*?</title>", new_title, content)
        
        new_strong = f"<strong>{goal_names[i]}</strong>"
        content = re.sub(r"<strong>.*?</strong>", new_strong, content, count=1)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
    except FileNotFoundError:
        pass
