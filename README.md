# C1FAPP-API-Client

C1fapp API Client

[**C1fApp**](https://www.c1fapp.com/) is a threat feed aggregation application, providing a single feed, both Open Source and private. 

>C1FAPP is my favorite threat feed agreegator out there!!!

## Requirements

* requests
* prettytable
* colorama
* termcolor

## Help

```
usage: c1fapp.py [-h] -s SEARCH -k API [-v]

C1fapp Threat Intel Search.

optional arguments:
  -h, --help  show this help message and exit
  -s SEARCH   Search ip/domain/url
  -k API      c1fapp api key
  -v          show program's version number and exit

```


## Example

>python c1fapp.py -s paypal-required-action.com -k \<api_key>

```
+------------+---------------------------------+--------------------------------------------+------------+------------+------------+-----------------+-------+---------------------+
| feed label |              domain             |                description                 | assessment | confidence | reportime  |    ipaddress    |  asn  |       derived       |
+------------+---------------------------------+--------------------------------------------+------------+------------+------------+-----------------+-------+---------------------+
| Phishtank  |    paypal-required-action.com   |                   Other                    |  phishing  |     95     | 2018-04-01 | 162.219.251.133 | 33494 |        direct       |
| Phishtank  |    paypal-required-action.com   |                   PayPal                   |  phishing  |     95     | 2018-04-01 | 162.219.251.133 | 33494 |        direct       |
| Phishtank  |    paypal-required-action.com   |                   Other                    |  phishing  |     95     | 2018-04-05 | 162.219.251.133 | 33494 |        direct       |
| Phishtank  |    paypal-required-action.com   |                   Other                    |  phishing  |     95     | 2018-04-03 | 162.219.251.133 | 33494 |        direct       |
| Phishtank  |    paypal-required-action.com   |                   Other                    |  phishing  |     95     | 2018-04-04 | 162.219.251.133 | 33494 |        direct       |
| Phishtank  |    paypal-required-action.com   |                   PayPal                   |  phishing  |     95     | 2018-04-04 | 162.219.251.133 | 33494 |        direct       |
| Phishtank  |    paypal-required-action.com   |                   Other                    |  phishing  |     95     | 2018-04-02 | 162.219.251.133 | 33494 |        direct       |
| Phishtank  |    paypal-required-action.com   |                   Other                    |  phishing  |     95     | 2018-04-05 | 162.219.251.133 | 33494 |        direct       |
| Phishtank  |    paypal-required-action.com   |                   PayPal                   |  phishing  |     95     | 2018-04-05 | 162.219.251.133 | 33494 |        direct       |
| Phishtank  |    paypal-required-action.com   |                   Other                    |  phishing  |     95     | 2018-04-04 | 162.219.251.133 | 33494 |        direct       |
| Phishtank  |    paypal-required-action.com   |                   Other                    |  phishing  |     95     | 2018-04-01 | 162.219.251.133 | 33494 |        direct       |
| Phishtank  |    paypal-required-action.com   |                   Other                    |  phishing  |     95     | 2018-04-03 | 162.219.251.133 | 33494 |        direct       |
| Phishtank  |    paypal-required-action.com   |                   PayPal                   |  phishing  |     95     | 2018-04-03 | 162.219.251.133 | 33494 |        direct       |
| Phishtank  |    paypal-required-action.com   |                   Other                    |  phishing  |     95     | 2018-04-02 | 162.219.251.133 | 33494 |        direct       |
| Phishtank  |    paypal-required-action.com   |                   PayPal                   |  phishing  |     95     | 2018-04-02 | 162.219.251.133 | 33494 |        direct       |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-05 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-05 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-10 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-13 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-15 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-16 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-12 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-11 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-06 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-06 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-09 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-10 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-02 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-02 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-04 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-01 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-14 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-24 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-22 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-23 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-27 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-27 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-25 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-28 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-30 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-26 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-31 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |  www.paypal-required-action.com |                   Other                    |  phishing  |     95     | 2018-04-01 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |          gsmfaizan.com          |                   Other                    |  phishing  |     95     | 2018-04-01 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  | mail.paypal-required-action.com |                   Other                    |  phishing  |     95     | 2018-04-01 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-04-01 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-04-05 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-04-05 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |  www.paypal-required-action.com |                   Other                    |  phishing  |     95     | 2018-04-05 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |          gsmfaizan.com          |                   Other                    |  phishing  |     95     | 2018-04-05 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |  www.paypal-required-action.com |                   Other                    |  phishing  |     95     | 2018-04-03 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |  www.paypal-required-action.com |                   Other                    |  phishing  |     95     | 2018-04-03 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |          gsmfaizan.com          |                   Other                    |  phishing  |     95     | 2018-04-03 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-04-04 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |  www.paypal-required-action.com |                   Other                    |  phishing  |     95     | 2018-04-04 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |          gsmfaizan.com          |                   Other                    |  phishing  |     95     | 2018-04-04 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-04-02 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |          gsmfaizan.com          |                   Other                    |  phishing  |     95     | 2018-04-06 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-04-06 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-04-07 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-04-08 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-04-09 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-04-10 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |          gsmfaizan.com          |                   Other                    |  phishing  |     95     | 2018-04-10 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-04-11 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |          gsmfaizan.com          |                   Other                    |  phishing  |     95     | 2018-04-11 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-04-11 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-15 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-14 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-16 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-13 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-08 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-08 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-12 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-11 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-03 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-03 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-04 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-01 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-09 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-17 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-17 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-21 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-18 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-18 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-21 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-22 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-29 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-29 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-30 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-28 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-25 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-24 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-23 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-19 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-19 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-20 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-03-20 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-03-26 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |  www.paypal-required-action.com |                   Other                    |  phishing  |     95     | 2018-04-05 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |  www.paypal-required-action.com |                   Other                    |  phishing  |     95     | 2018-04-04 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-04-04 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |          gsmfaizan.com          |                   Other                    |  phishing  |     95     | 2018-04-07 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-04-07 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-04-01 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |      dancarvalhoead.com.br      |                   Other                    |  phishing  |     95     | 2018-04-03 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  | mail.paypal-required-action.com |                   Other                    |  phishing  |     95     | 2018-04-03 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-04-02 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-04-03 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |  www.paypal-required-action.com |                   Other                    |  phishing  |     95     | 2018-04-02 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |          gsmfaizan.com          |                   Other                    |  phishing  |     95     | 2018-04-02 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  | mail.paypal-required-action.com |                   Other                    |  phishing  |     95     | 2018-04-02 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-04-06 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-04-10 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-04-09 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |         smbagencies.com         |                   Other                    |  phishing  |     95     | 2018-04-08 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |          gsmfaizan.com          |                   Other                    |  phishing  |     95     | 2018-04-08 | 162.219.251.133 | 33494 | indirect_resolve_ip |
| Phishtank  |          gsmfaizan.com          |                   Other                    |  phishing  |     95     | 2018-04-09 | 162.219.251.133 | 33494 | indirect_resolve_ip |
|  SpamHaus  |    paypal-required-action.com   | Static UBE sources, verified spam services |    Spam    |     80     | 2018-04-11 | 162.219.251.133 | 33494 |      ip_resolve     |
+------------+---------------------------------+--------------------------------------------+------------+------------+------------+-----------------+-------+---------------------+

```