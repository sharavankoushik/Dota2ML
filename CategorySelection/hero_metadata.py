import json

class HeroMetadata:
     def __init__(self, modelroot='dotaml-master'):
        metadata_path = os.path.join(model_root, 'heroStats.json')
        self.hero_stats = json.loads(metadata_path)

    def __repr__(self):
        return '<HeroMetadata %r>' % self.metadata_path

    def __str__(self):
        return self.name

    def retrieve_hero_metadata(self,my_team,their_team):
        [for i in my_team]
