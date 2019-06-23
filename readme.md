# WSS

WSS (WHK Subdomains Scanner) is a tool for *pentesters* dedicated to the search
of subdomains.


## Requirements

- Python 3
- Google API-Key in `modules/google.py` (optional)


## Installation

It is required to install the dependencies using pip3:

    pip3 install -r requirements.txt


## Use

Syntax:
    
    python3 wss.py [hostname]

Example:

    python3 wss.py starbucks.com


## Advantage

In addition to looking at already known services, it is able to use brute force
by obtaining fresh subdomains without using databases. It also delivers a tree
of associated IP addresses to know redundant subdomains, saving time in service
review.


## Methods

Currently supports the following methods:

- Test AXRF Zone transfer
- Find using dns queries (TXT, MX, NS, etc)
- Find in virustotal.com
- Find in robtex.com
- Find in crt.sh
- Find in cetificatedetails.com
- Find in google.com
- Find in bing.com
- Find in dnsdumpster.com
- Bruteforcing using 1 to 4 chars
- Using dictionary with known subdomains


## Out

- Print a tree of ip address with each subdomain in group.
- Write a file with the printed tree.