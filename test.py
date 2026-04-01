datas = [{"id": 1, "title": "danser", "priority": "low", "status": "done"}, {"id": 2, "title": "Ranger salon", "priority": "low", "status": "on going"}, {"id": "3", "title": "Ranger salon", "priority": "mid", "status": "on going"}, {"id": 4, "title": "Ranger salon", "priority": "low", "status": "on going"}, {"id": "5", "title": "Ranger salon", "priority": "high", "status": "on going"}, {"id": 6, "title": "Ranger salon", "priority": "low", "status": "on going"}]

# print(sorted(datas, key=lambda x: x['priority'] == 'low'))

print(sum(1 for el in datas if el['priority'] == 'low'))

# li = [1, 2, 3, 4, 4, 4]
# print(li.count(4))