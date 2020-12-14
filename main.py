#! Python3
from fbBotClass import NewPost
import yaml


# Getting credentials from globalresource,yaml
with open('docs/globalresource.yaml', 'r') as f:
    cred = yaml.load(f, Loader=yaml.FullLoader)
f.close()

# Defining object fb of class fbBotClass
fb = NewPost(
    user = cred["email"],
    passwd = cred["secret"]
)

# Running method run from object class fbBotClass
fb.run(msg = " Oi, eu sou um robô :)")
