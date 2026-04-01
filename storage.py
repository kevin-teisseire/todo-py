import os, json

folder = os.path.dirname(__file__)
file_path = os.path.join(folder, 'tasks.json')

def loadF():
    datas = [] # list of dictionaries (tasks)
    try:
        with open(file_path, 'r') as f:
            datas = json.load(f)
    except FileNotFoundError as err:
        return []
    return datas

def saveF(datas):
    if datas is not None:
        with open(file_path, 'w') as f:
            json.dump(datas, f)
