* Alpha version 0.00001 * For devs only!

# Creation of a job search robot spider (2020/11/18)

On Debian system,

* ## Start the MongoDB using Docker:

``` sudo apt install docker.io ```  
``` sudo docker run -d -p 27017:27017 -v ~/src/data/mongo-docker:/data/db --name mongodb mongo:4.2 ```  
``` sudo docker exec -it mongodb mongo  ```(if any error, try before: 'sudo docker exec -it mongodb mongo)```


* ## Conda env installation:

```
sudo apt install conda
conda install conda pymongo flask scrapy
```

* ## To start the robot: (Download time sets at 200ms and user agent show Opera Browser)
```
scrapy runspider flashbot.py --set=USER_AGENT="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 OPR/72.0.3815.320
```

* ## To start locally, the web server:

In the rss_blog/ directory,
```
export FLASK_ENV=development  
export FLASK_APP=app.py  
flask run  
```

with the message:
```
WARNING: This is a development server. Do not use it in a production deployment.  
   Use a production WSGI server instead.  
 * Debug mode: off  
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You can launch your browser with url : ```http://127.0.0.1:5000/search```  
And try to browse the data with your own words!

Have fun!

[bigjim](https://github.com/CLiNTPELiX/simplon-brief3/blob/main/bigjim.jpg)
