# pyport
Pyport is a strong portscanner based on python !

# Setup
__My OS was ubuntu when i code this so commands is for ubuntu, you may need to customize them by your OS.__

* First you need to install these => 
  * python3
  * pip3
  * neofetch
  
```shell
sudo apt install python3 pip3 neofetch
```

* I used these modules =>
  * socket 
  * colorama
  * time
  * os
  * sys
  

> if you lost any, you can install it by this command :
```python
pip3 install [Module-Name]
```
Clone the Repo :
```python
git clone https://github.com/sadult/pyport
```
CD: 
```python 
cd pyport
```
By defualt it scanns from port `1` to `9999`
you can custmoize it from `2` - `65535`
in line `64`
  
```python
for port in range(1, 9999):
```
change 
`9999`
value, then :
```python
python3 pyport.py 
```
# Me
[Mercad](https://t.me/sadult)   |   [Website](https://mercads.ir)   |   [Github](https://github.com/sadult)   ~
