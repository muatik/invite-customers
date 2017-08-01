[![Build Status](https://travis-ci.org/muatik/invite-customers.svg?branch=master)](https://travis-ci.org/muatik/invite-customers)

references about calculating distance between two points(latitude, longtitude):
* https://en.wikipedia.org/wiki/Great-circle_distance
* http://andrew.hedges.name/experiments/haversine/
* http://www.movable-type.co.uk/scripts/latlong.html


### Run
```sh
git clone git@github.com:muatik/invite-customers.git
cd invite-customers
python src/app.py
```

### Test
Install pytest, `pip install pytest` and issue the following commands.
```sh
git clone git@github.com:muatik/invite-customers.git
cd invite-customers
pytest src/tests
```