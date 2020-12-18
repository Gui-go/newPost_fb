#! Python3
from fbBotClass import NewPost
import yaml


if __name__ == '__main__':
    # Getting credentials from globalresource,yaml
    with open('conf/globalresource.yaml', 'r') as f:
        cred = yaml.load(f, Loader=yaml.FullLoader)

    # Defining object fb of class fbBotClass
    fb = NewPost(
        user = cred["email"],
        passwd = cred["secret"]
    )

    # Running method run from object class fbBotClass
    fb.run(msg = " Oi, eu sou um robô :)")

