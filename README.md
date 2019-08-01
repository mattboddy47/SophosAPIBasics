# SophosAPIBasics
Basic tools for making requests to the Sophos Central API

# Simple GET Request
The simple GET request provides a very simple framework for doing a GET request to the Sophos API using requests

The Python file has been fully commented to help understand what is going on.  Please change the headers to include your own API key and authentication token which you'll find within your Sophos Central account.   

# Sophos Device ID from IP
This simple script allows you to search for a Sophos device ID using an IP address of the device as the search peramiter.  The aim of this is to allow for third party products like firewalls or honeypots to search for offending local IP addresses to help corrolate events from other vendors. 
You will need:
- your API URL
- your X-API-Key
- your your Authorization code starting with Basic
- The IP address which you'd like to search for
