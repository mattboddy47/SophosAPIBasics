# SophosAPIBasics
Basic tools for making requests to the Sophos Central API

# SimpleGETRequest.py
The simple GET request provides a very simple framework for doing a GET request to the Sophos API using requests

The Python file has been fully commented to help understand what is going on.  Please change the headers to include your own API key and authentication token which you'll find within your Sophos Central account.   

# SophosDeviceIDfromIP.py
This simple script allows you to search for a Sophos device ID using an IP address of the device as the search peramiter.  The aim of this is to allow for third party products like firewalls or honeypots to search for offending local IP addresses to help corrolate events from other vendors. 
You will need:
- your API URL
- your X-API-Key
- your your Authorization code starting with Basic
- The IP address which you'd like to search for

# CreateEndpointCSVReport.py
This script allows you to export a CSV report from Sophos Central of device encryption status, endpoint last updated status, computer name and IP's associated with the device.  The aim of this script is to replicate the report provided by SQL commands on the older SEC console.
You will need:
- your API URL
- your X-API-Key
- your your Authorization code starting with Basic
- The IP address which you'd like to search for
