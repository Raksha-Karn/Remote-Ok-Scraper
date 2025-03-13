
# RemoteOk Job Scraper


This scraper scrapes https://remoteok.com using **Selenium**. It performs the following tasks:

1.  **Extracts job links**: Runs a Selenium script to search for a job and collect all relevant job links, storing them in a file.
2.  **Scrapes job details**: Another Selenium script reads the stored links, opens each job page, and extracts relevant data.
3.  **Implements rotating proxies & user agents**: To prevent detection and blocking, the scraper rotates proxies and user agents dynamically.


## Installation

Clone this repository:

```sh
$ git clone git@github.com:Raksha-Karn/Remote-Ok-Scraper.git
```

Install the dependencies:

```sh
$ pip install -r requirements.txt
```
