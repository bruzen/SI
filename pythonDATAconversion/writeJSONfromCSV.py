

import csv
import json
import io

f = open( 'piedance.csv', 'rb' )
reader = csv.DictReader( f)
out = json.dumps( [ row for row in reader ] )
print out

with io.open('piedance.json', 'w', encoding='utf-8') as f:
  f.write(unicode(out))

