
from jsonschema import validate, ValidationError
import json, sys

with open(sys.argv[1]) as f:
    data = json.load(f)

with open("scenario_schema.json") as f:
    schema = json.load(f)

try:
    validate(instance=data, schema=schema)
    print("✅ Scenario JSON is valid")
except ValidationError as e:
    print("❌ Validation error:
")
    print(e)
    sys.exit(1)
