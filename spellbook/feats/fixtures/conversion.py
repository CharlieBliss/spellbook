import json
import re
import pprint

featsRaw = open('spellbook/feats/fixtures/base.txt').read()

feat_list = featsRaw.splitlines()

def matchFeat(string):
    return re.match(r'General|Skill|Death|Emotion|Fear|Manipulate', string)


filtered = list(filter(lambda x: not matchFeat(x), feat_list))
filtered.insert(332, 'Skill Training Feat 1')

indices = [index for index, element in enumerate(filtered) if re.search(r'Feat *[0-9]', element)]

index = 0
chunkedFeats = []
for item in indices:
    chunk = slice(index, item)
    subset = filtered[chunk]
    chunkedFeats.append(subset)
    index = item

def mapItem(feat_list):
    obj = {}
    obj['name'] = feat_list[0]
    if feat_list[1].__contains__('prereq'):
        obj['prereq'] = feat_list[1]
    else:
        obj['description'] = feat_list[1]
    if len(feat_list) > 2:
        obj['description'] = feat_list [2]
    for n in feat_list:
        if n.__contains__('Critical Failure'):
            obj['crit_failure'] = n
        elif n.__contains__('Failure'):
            obj['fail'] = n
        if n.__contains__('Critical Success'):
            obj['crit_success'] = n
        elif n.__contains__('Success'):
            obj['success'] = n
        if n.__contains__('Special\xa0'):
            obj['special'] = n

    return obj

kill_empty = list(filter(lambda item: len(item), chunkedFeats))

objects = list(map(lambda item: mapItem(item), kill_empty))


for obj in objects:
    name, level = obj['name'].split('Feat')
    obj['name'] = name.strip()
    obj['level'] = int(level.strip()[0:1])


def modify(feats):
    newObj = []

    for index, feat in enumerate(feats):
        top = {}
        top['model'] = "feats.feat"
        top['pk'] = index + 1
        top['fields'] = feat
        newObj.append(top)

    return newObj

jsonFeats = (json.dumps(modify(objects)))

open('spellbook/feats/fixtures/feats.json', 'w').write(jsonFeats)