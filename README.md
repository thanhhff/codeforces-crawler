# CodeForces-Crawler 

A scrapy-based crawler for all **submissions** (including source code) of any specific problems on www.codeforces.com.

Since the [provided APIs](https://codeforces.com/api/help/objects) of CodeForces is not so strong as Github, I endeavored to process the front-end requests within Codeforces websites. Now the crawler is not limited to API restrictions.  

Tutorial: https://www.datacamp.com/community/tutorials/making-web-crawlers-scrapy-python

**Prerequisites**:  
- [Python 3 or above](https://www.python.org/)
- [Anaconda](https://www.anaconda.com/)

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# Usage:
### Step 0 - Set up the virtual enviroment (Optional)
This is an optional (but really **recommended**) step.
```
Use anaconda to create virtual environment.
```

### Step 1 - Install all the required dependencies
```
pip install -r requirements.txt
```

### Step 2 - Start crawling

```
Crawl content from id in `contest-info.csv` file. (Please check this file!)
```
```
cd codeforces_crawler
scrapy crawl cf_submission
```
then you are able to restore this crawler with the **same command**, whenever the crawling process is interrupted.


# About the scraped item - *Submission*
An scraped entity represents a submission with the structure below:

| Key           | Required     | Type   | Description                                                                                                                    |
| ------------- | ------------ | ------ | ------------------------------------------------------------------------------------------------------------------------------ |
| submission_id | yes          | String | the ID of this submission                                                                                                      |
| verdict       | yes          | String | the status of this submission (e.g., "OK","RUNTIME_ERROR")                                                                                                  |
| round_id      | yes          | String | the round number of the problem                                                                                                |
| problem_name  | yes          | String | the name of the problem                                                                                                        |
| problem_url   | no, optional | String | the link url of the problem (yet not crawled)                                                                                       |
| source_code   | yes          | String | critical, the stringify content of the source code                                                                             |
| language      | yes          | String | the programming language of the source code (e.g., "GNU C++11")   |
 

# License
MIT License
Copyright (c) 2018 LAB-SSE

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
