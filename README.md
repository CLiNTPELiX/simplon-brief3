# Creation of robot spider (2020/11/18)

On Debian system,

* ## Start the MongoDB using Docker:

``` sudo apt install docker.io ```  
``` sudo docker run -d -p 27017:27017 -v ~/src/data/mongo-docker:/data/db --name mongodb mongo:4.2 ```  
``` sudo docker exec -it mongodb mongo  (```if any error, try before: 'sudo docker exec -it mongodb mongo```)


* ## To start the robot (): 
```
scrapy runspider flashbot.py --set=USER_AGENT="OPERRRRRRRRRRRRRRRRRRRRRA"
```

* ## To start locally, the web server:
(keywords used are saved in thesaurus variable inside flashbot.py, you can try with your own)

Dans le repertoire rss_blog,
```
export FLASK_ENV=development  
export FLASK_APP=app.py  
flask run  
```

have fun!