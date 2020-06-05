class jsonutils:
    
    _schema = {
    "type": "object",
    "required": ["title", "description", "component"]
    }
    
    def checkRequest(self, jsonDocument):

        import jsonschema
        import json

        try:
            tfsrq = json.loads(jsonDocument)
            jsonschema.validate(tfsrq, self._schema)
            print("Valid JSON")
            return 1
        except jsonschema.exceptions.ValidationError as e:
            print("Invalid JSON:", e)
        except json.decoder.JSONDecodeError as e:
            print("Not JSON:", e)