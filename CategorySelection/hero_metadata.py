import json
import os
from collections import defaultdict


def retrieve_hero_metadata():
    model_root = 'CategorySelection'
    metadata_path = os.path.join(model_root, 'stats.json')
    hero_stats = json.load(open(metadata_path))
    list_hero_roles = set()
    roles_ids = defaultdict(list)
    # create a dictionary with key as hero roles and values as list of hero ids
    for i in range(len(hero_stats)):
        for j in hero_stats[i].get("roles"):
            roles_ids[j].append(hero_stats[i].get("id"))
    return roles_ids


retrieve_hero_metadata()
