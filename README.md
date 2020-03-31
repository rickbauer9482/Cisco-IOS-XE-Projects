# Cisco-IOS-XE-Projects
Various scripting projects working with Cisco IOS-XE
This topic provides an overview of some of the Cisco IOS XE API.

REST-based API

HTTP(S) Transport

Uses YANG data models

JSON/XML Encoding

Content-Type & Accept Headers:

application/vnd.yang.data+json

application/vnd.yang.data+xml

Currently must exit configuration mode after making a change for it to be readable via RESTCONF

RESTCONF exposes a web-based interface in a consistent fashion in that it is just like any other REST API. The only differences are that you need to use specific Headers and that the URL and data is driven by YANG models.

Two of the common headers are Content-Type and Accept when working with RESTful APIs. They are often set to application/json or application/xml. While there are a few variations supported for IOS XE, the common ones are:

application/vnd.yang.data+json

application/vnd.yang.data+xml

Also note that the REST interface that is exposed by IOS XE is the same interface that is exposed by the Cisco NSO.

restconf 
! 
username <username> privilege 15 password <password>  
! 
ip http server 
ip http secure-server 
