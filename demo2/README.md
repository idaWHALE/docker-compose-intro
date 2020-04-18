# Demo2 - Containers Logging to ELK using Gelf Driver

Please follow these steps:

1. Please ensure that you have Docker and Docker-compose ready in your local machine.

```
$ docker --version
$ docker-compose --version
```

2. After you clone this repository, please change your directory to demo1

```
$ cd demo2
```

3. Then you only need to execute this command:

```
$ docker-compose up
```

4. Open your browser and follow these steps:

- open http://localhost:5601/
- find "Management" menu on the left sidebar
- choose "Index Patterns" menu on the left section under "Kibana"
- hit "Choose Index Pattern" button on the top right corner
- put `logstash-*` on the Index Pattern field then choose "Next Step"
- choose "@timestamp" to be used as time filter in the section 2. Now your index is ready
- find "Discover" menu on the left sidebar and click it
- now you are able to explore anything to your gelf logs

Hopefully it's working for you!.