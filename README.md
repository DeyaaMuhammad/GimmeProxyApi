# GimmeProxyApi
Python API Package for gimmeproxy.com .


# API Parameters
![gimmeproxyapi](https://user-images.githubusercontent.com/16267182/35398153-eb5e9374-01f9-11e8-9cf0-1bf646ae2732.PNG)


### Examples

### Choosing Country :
```
proxy = GimmeProxyAPI(country="USA,UK")
print proxy.get_ip_port()
```
#### Result:
`200.21.21.157:8080`


### Choosing Protocol :
```
proxy = GimmeProxyAPI(protocol="http")
print proxy.get_curl()
```
#### Result:
`http://200.21.21.157:8080`


