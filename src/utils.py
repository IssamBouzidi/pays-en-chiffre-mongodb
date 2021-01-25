import json
from bson import json_util
from bson.json_util import dumps

class Utils:

    @classmethod
    def get_tranche(cls, density):
        """
        function return a tranche of a density
        Args:
            density (int): density of a country

        Returns:
            stirng: tranche of a density
        """
        if 0 < density <= 100:
            return 'Tranche 1'
        elif 100 < density <= 1000:
            return 'Tranche 2'
        elif 1000 < density <= 10000:
            return 'Tranche 3'
        elif 10000 < density:
            return 'Tranche 4'
        else:
            return 'Tranche Inconnue'
    
    
    @classmethod
    def parse_json(cls, data):
        return json.loads(json_util.dumps(data))

    @classmethod
    def toJson(cls, data):
        """Convert Mongo object(s) to JSON"""
        return json.dumps(data, default=json_util.default)