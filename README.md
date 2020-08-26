# Connecticut Zip to Town Crosswalk

The `data/zip2town.csv` file contains a crosswalk between CT zipcodes and
towns in CT. There are 282 zipcodes and 169 towns. **Note that in real life,
some zipcodes cross town boundaries, therefore this crosswalk is approximate**.

| zip5|town|county|town_fips|
|--|--|--|--|
|06810|Danbury|Fairfield|0900118500 |
|06608|Bridgeport|Fairfield|0900108070 |
|06468|Monroe|Fairfield|0900148620 |
|06089|Simsbury|Hartford|0900368940 |
|06820|Darien|Fairfield|0900118850 |


To prevent Excel from transforming zipcodes and town FIPS codes to numbers automatically
(which leads to missing leading 0s), do the following:

1. Open Excel, New workbook
1. Go to File > Import > CSV file
1. Choose file, and select "text" as type of zip5 and town_fips columns


### How it was generated
In QGIS, open zipcode boundaries, calculate their centroids, and perform nearest neighbor spatial join
(NNJoin plugin) to assign the nearest town. All centroids fall within one
town, so the generated `distance` column will have all 0s.

### Source datasets

* Connecticut town boundaries: https://data.ct.gov/Government/Town-Boundary-Index-Map/evyv-fqzg
* Connecticut zipcode boundaries: https://data.ct.gov/Government/Zip-Code-Tabulation-Area-Boundaries/n7kw-xx5z

### License

Released under MIT license. Feel free to use for all sorts of projects. We will appreciate if you credited CTData Collaborative, although this is not required.
