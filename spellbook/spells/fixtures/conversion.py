import json
import pprint

spells = json.loads(open('spellbook/spells/fixtures/spells.json').read())


def modify(spells):
    newObj = []

    for index, spell in enumerate(spells.values()):
        top = {}
        top['model'] = "spells.spell"
        top['pk'] = index + 1
        if spell['description'].get('subsections'):
            spell['success'] = spell['description']['subsections'].get('success')
            spell['crit_success'] = spell['description']['subsections'].get('crit')
            spell['crit_failure'] = spell['description']['subsections'].get('crit-fail')
            spell['fail'] = spell['description']['subsections'].get('failure')
        spell['verbal'] = 'aV' in spell['casting']
        spell['somatic'] = 'aS' in spell['casting']
        spell['id'] = index + 1
        spell['material'] = spell.get('requirements') or spell.get('cost') or 'aM' in spell['casting']
        spell['description'] = spell['description']['main']
        spell['casting_time'] = spell.get('casting-time')
        top['fields'] = spell
        del spell['casting']
        if spell.get('casting-time'):
            del spell['casting-time']
        if spell.get('requirements'):
            del spell['requirements']
        if spell.get('cost'):
            del spell['cost']
        newObj.append(top)

    return newObj

jsonSpells = (json.dumps(modify(spells)))

open('spellbook/spells/fixtures/spells2.json', 'w').write(jsonSpells)


# pprint.pprint(next(iter(spells.key())))
