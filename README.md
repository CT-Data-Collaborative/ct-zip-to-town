# Connecticut Zip to Town Crosswalk

The `data/2020zip-to-town.csv` and `data/2010zip-to-town.csv` files contain a crosswalk between CT zipcodes (technically ZCTAs,
or zipcode tabulation areas, which are geographic approximations for zipcodes) and towns in CT.

For 2020, there are 289 zipcodes and 169 towns in the state, and the crosswalk
is a many-to-one relationship, meaning each zipcode points ("belongs") to only one town,
and one town can be served by one or more zipcodes.

**Because some zipcodes cross town boundaries and may serve more than one town,
this crosswalk is approximate**.

Union and Lisbon are not in the crosswalk because zipcode centroids did not fall
inside town boundaries (see methodology below).

To prevent Excel from transforming zipcodes to numbers automatically
(which leads to missing leading 0s), do the following:

1. Open Excel, New workbook
1. Go to File > Import > CSV file
1. Choose file, and select "text" as type of 2020zip5


## How it was generated
In QGIS, open zipcode boundaries, calculate their centroids, and perform nearest neighbor spatial join
(NNJoin plugin) to assign the nearest town. All centroids fall within one
town, so the generated `distance` column should have `0` values everywhere.

### Source datasets

* Connecticut town boundaries: https://data.ct.gov/Government/Town-Boundary-Index-Map/evyv-fqzg
* Connecticut zipcode boundaries: https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2022&layergroup=ZIP+Code+Tabulation+Areas

## License

Released under MIT license. Feel free to use for all sorts of projects. We will appreciate if you credited CTData Collaborative, although this is not required.
