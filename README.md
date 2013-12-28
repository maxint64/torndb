Introduce                                                                                                                          
---------                                                                                      
I forked this repository from Torndb(https://github.com/bdarnell/torndb) and make it could connect different databases using     
arguments in config file named ``dbconf.py``.                                                  
                                                                                                
Usage                                                                                          
-----                                                                                          
```python                                                                                      
                                                                                              
import torndb                                                                                  
#connect using default arguments                                                               
db = torndb.connect()                                                                          
#or connect to a test database                                                                 
db = torndb.connect("test")                                                                    
                                                                                              
```                                                                                            
                                                                                                
Sample Config                                                                                  
-------------                                                                                  
```python                                                                                      
                                                                                                
conf["default"]["host"] = "localhost"                                                          
conf["default"]["database"] = "database"                                                       
conf["default"]["user"] = "user"                                                               
conf["default"]["password"] = "password"                                                       
conf["default"]["max_idle_time"] = 7*3600                                                      
conf["default"]["connect_timeout"] = 0                                                         
conf["default"]["time_zone"] = "+0:00"                                                         
                                                                                               
```
