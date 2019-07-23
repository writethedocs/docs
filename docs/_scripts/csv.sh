#!/bin/bash

# # NA 2016
# cat ~/Downloads/Final\ Talks\ -\ Schedule.csv |csvcut -x -c 2,3| head -n 25 |csvjson -i 4 > ../_data/na-2016-day-1.json
# cat ~/Downloads/Final\ Talks\ -\ Schedule.csv |csvcut -x -c 2,3| tail -n 27 |csvjson -i 4 > ../_data/na-2016-day-2.json
#
# #EU 2016
#
# cat ~/Downloads/Final\ Talks\ EU\ 2016\ -\ Schedule.csv | csvcut -x -c 1,2 | head -n 25 | csvjson -i 4 > ../_data/eu-2016-day-1.json
# cat ~/Downloads/Final\ Talks\ EU\ 2016\ -\ Schedule.csv | csvcut -x -c 1,2 | tail -n 24 | csvjson -i 4 > ../_data/eu-2016-day-2.json

# NA 2017

#cat ~/Downloads/Write\ the\ Docs\ Portland\ 2017\ Schedules\ -\ Main\ Filled.csv |csvcut -x -c 1,2 | head -n 31 |csvjson -I -i 4 > ../_data/na-2017-day-1.json
#cat ~/Downloads/Write\ the\ Docs\ Portland\ 2017\ Schedules\ -\ Main\ Filled.csv |csvcut -x -c 1,2 | tail -n 23 |csvjson -I -i 4 > ../_data/na-2017-day-2.json
# cat ~/Downloads/Write\ the\ Docs\ Portland\ 2017\ Schedules\ -\ Writing\ Day.csv | csvcut -x -c 1,2 | head -n 25 | csvjson -I -i 4 > ../_data/na-2017-writing-day.json

# EU Empty schedule

#cat ~/Downloads/Write\ the\ Docs\ Prague\ 2017\ Schedules\ -\ Main\ Conference.csv |csvcut -x -c 1,2 | head -n 22 |csvjson -I -i 4 | python -c 'import sys, yaml, json; yaml.safe_dump(json.load(sys.stdin), sys.stdout, default_flow_style=False)' > ../_data/eu-2017-day-1.yaml
#cat ~/Downloads/Write\ the\ Docs\ Prague\ 2017\ Schedules\ -\ Main\ Conference.csv |csvcut -x -c 1,2 | tail -n 20 |csvjson -I -i 4 | python -c 'import sys, yaml, json; yaml.safe_dump(json.load(sys.stdin), sys.stdout, default_flow_style=False)' > ../_data/eu-2017-day-2.yaml

# EU Filled schedule

#cat ~/Downloads/Write\ the\ Docs\ Prague\ 2017\ Schedules\ -\ Main\ Filled.csv | head -n 23 |csvjson -I -i 4 | python -c 'import sys, yaml, json; yaml.safe_dump(json.load(sys.stdin), sys.stdout, default_flow_style=False)' > ../_data/eu-2017-day-1.yaml
#cat ~/Downloads/Write\ the\ Docs\ Prague\ 2017\ Schedules\ -\ Main\ Filled.csv | tail -n 20 |csvjson -I -i 4 | python -c 'import sys, yaml, json; yaml.safe_dump(json.load(sys.stdin), sys.stdout, default_flow_style=False)' > ../_data/eu-2017-day-2.yaml

# AU 2017

#cat ~/Downloads/Write\ the\ Docs\ Day\ Australia\ 2017\ -\ Main\ Conference.csv |csvcut -x -c 1,2 | head -n 7 |csvjson -I -i 4 | python -c 'import sys, yaml, json; yaml.safe_dump(json.load(sys.stdin), sys.stdout, default_flow_style=False)' > ../_data/au-2017-AM.yaml
#cat ~/Downloads/Write\ the\ Docs\ Day\ Australia\ 2017\ -\ Main\ Conference.csv |csvcut -x -c 1,2 | tail -n 12 |csvjson -I -i 4 | python -c 'import sys, yaml, json; yaml.safe_dump(json.load(sys.stdin), sys.stdout, default_flow_style=False)' > ../_data/au-2017-PM.yaml

# NA  2018

#cat ~/Downloads/Write\ the\ Docs\ Portland\ 2018\ Schedules\ -\ Main\ Filled.csv | head -n 25 |csvjson -I -i 4 | python -c 'import sys, yaml, json; yaml.safe_dump(json.load(sys.stdin), sys.stdout, default_flow_style=False)' > ../_data/na-2018-day-1.yaml
#cat ~/Downloads/Write\ the\ Docs\ Portland\ 2018\ Schedules\ -\ Main\ Filled.csv | tail -n 18 |csvjson -I -i 4 | python -c 'import sys, yaml, json; yaml.safe_dump(json.load(sys.stdin), sys.stdout, default_flow_style=False)' > ../_data/na-2018-day-2.yaml

# Prague 2018

# cat ~/Downloads/Prague\ Speakers\ \&\ Schedules\ -\ Speaker\ Schedule.csv | head -n 25 |csvjson -I -i 4 | python -c 'import sys, yaml, json; yaml.safe_dump(json.load(sys.stdin), sys.stdout, default_flow_style=False)' > ../_data/eu-2018-day-1.yaml
# cat ~/Downloads/Prague\ Speakers\ \&\ Schedules\ -\ Speaker\ Schedule.csv | tail -n 18 |csvjson -I -i 4 | python -c 'import sys, yaml, json; yaml.safe_dump(json.load(sys.stdin), sys.stdout, default_flow_style=False)' > ../_data/eu-2018-day-2.yaml

# Portland 2019

#cat cat ~/Downloads/Portland\ 2019\ Schedules\ -\ Writing\ Day.csv | csvjson -I -i 4 | python -c 'import sys, yaml, json; yaml.safe_dump(json.load(sys.stdin), sys.stdout, default_flow_style=False)' > ../_data/portland-2019-writing-day.yaml
#cat ~/Downloads/Portland\ 2019\ Schedules\ -\ Main\ Filled.csv | head -n 25 |csvjson -I -i 4 | python -c 'import sys, yaml, json; yaml.safe_dump(json.load(sys.stdin), sys.stdout, default_flow_style=False)' > ../_data/portland-2019-day-1.yaml
#cat ~/Downloads/Portland\ 2019\ Schedules\ -\ Main\ Filled.csv | tail -n 20 |csvjson -I -i 4 | python -c 'import sys, yaml, json; yaml.safe_dump(json.load(sys.stdin), sys.stdout, default_flow_style=False)' > ../_data/portland-2019-day-2.yaml

# Prague 2019

cat ~/Downloads/Prague\ speaker\ confirmations\ 2019.csv | head -n 25 |csvjson -I -i 4 | python -c 'import sys, yaml, json; yaml.safe_dump(json.load(sys.stdin), sys.stdout, default_flow_style=False)' > ../_data/prague-2019-day-1.yaml
cat ~/Downloads/Prague\ speaker\ confirmations\ 2019.csv | tail -n 18 |csvjson -I -i 4 | python -c 'import sys, yaml, json; yaml.safe_dump(json.load(sys.stdin), sys.stdout, default_flow_style=False)' > ../_data/prague-2019-day-2.yaml
