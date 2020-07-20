# CHALLENGE RGRTECHNOLOGIA

Create a command-line application that, given a list of website URLs as input, visits them
and finds, extracts and outputs the websites’ logo image URLs and all phone numbers (e.g.
mobile phones, land lines, fax numbers) present on the websites.

### RUN THE PROJECT
* clone the project.

#### - NO IMAGE DOCKER
CREATE A VIRTUAL ENVIRONMENT IF YOU WANT 
```
cat website.txt | python3 -m pagescrap
```


#### - WITH IMAGE DOCKER
first let's create a volume for sharing the generated content
* important that the volume name is local to avoid errors
```
docker volumes create local
``` 

ready, now with the volume created let's start our docker image
```
docker build -t pagescrap .
```

now we can finally run our program and see the magic happening.
```
cat website.txt | docker run -i pagescrap:latest
```

##### ENDING

your results will be in a file called results.json and in your terminal