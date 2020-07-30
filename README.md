# SubGitter
"Subdomains" github dork  automation script. 

By the increasing number of sub-domains for a target, it is getting harder to check for every sub-domain in the github search manually. Hence the script which needs the file of subdomains and performs the code search on github with the results so we could find secrets at sneaky places.

# Usage

```
python3 github.py -h
usage: github.py [-h] -f FILE

Quick script to find github code searches for each subdomain

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  the file consisting of subdomains
```

# Requirements

Python3+

Install chromedriver

MAC - `brew cask install chromedriver` 

Linux - `sudo apt install chromium-chromedriver`


On MAC you might face this
Error: "chromedriver" cannot be opened because the developer cannot be verified. Unable to launch the chrome browser

Suggested Fix : `xattr -d com.apple.quarantine /usr/local/bin/chromedriver`


# Installation

Clone the repo `git clone https://github.com/Rnalter/SubGitter && cd SubGitter/`

Install project dependencies `pip install -r requirements.txt`

Update email and password in Github.py `vi github.py`

Run the tool via `python github.py --help`

# Running SubGitter

`python github.py -f subdomains.txt`

By default, runs chrome headless, in case you want see the browser performing the queries, comment out `options.add_argument("--headless")` line in github.py

# Output

```
python3 github.py -f subdomains.txt
4 for aclpushdb.ops.yahoo.com
14 for alms.ops.yahoo.com
1 for alpha.coname.ops.yahoo.com
2 for amf.ops.yahoo.com
1 for analytics.edge.ops.yahoo.com
0 for api-prod.vip.ops.yahoo.com
1 for api.brooklyn.ops.yahoo.com
4+ for api.cm.ops.yahoo.com
```

# Demo

[![Watch the video](https://j.gifs.com/zvjvNY.gif)](https://youtu.be/K7vGJD-MdSM)
