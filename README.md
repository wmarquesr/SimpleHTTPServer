# SimpleHTTPServer
A really simple HTTP Server/Client made in Python 3.

To run the server you must first change the path of the resources file to be accessed by it in the **MyHTTPServer.py** file.

Then the server is executed.

```
$ python MyHTTPServer.py
```

Then the client is executed, passing as parameter the server adress, it was used as standard 127.0.0.1.

```
$ python MyHTTPClient.py 127.0.0.1
```

With the server and the client running, simply perform the available requests (GET, POST, PUT, DELETE) for the resource file, or for any other address you wish.

```
$ GET rsc.txt
$ POST rsc.txt UFMG
$ PUT rsc.txt UFPE
$ DELETE rsc.txt UFMG
```
