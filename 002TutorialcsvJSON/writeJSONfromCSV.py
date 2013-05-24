

import csv
import json
import io

f = open( 'D2data/costs.csv', 'rb' )
reader = csv.DictReader( f, fieldnames = ( "policyname","mincost","maxcost" ) )
out = json.dumps( [ row for row in reader ] )
print out

with io.open('datab.json', 'w', encoding='utf-8') as f:
  f.write(unicode(out))

