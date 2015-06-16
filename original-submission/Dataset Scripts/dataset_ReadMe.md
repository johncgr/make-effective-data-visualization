### NanoDegree Project 5 Dataset ReadMe ###

1. The data was extracted from the Bureau of Labor Statistics public data API with the API.py script. 
  * More information: http://www.bls.gov/developers/api_signature.htm
  * Additional BLS webpage on Series ID's: http://www.bls.gov/help/hlpforma.htm#CU

2. I ran the json blob through another script bls_json_stripper.py to remove information I did not need and to set the data into the tidy data format.

3. Finally, because I couldn't pull all the data I needed off the API in one request I created csv_zipper.py to combine the individual pieces returned by the API into one tidy data set.
