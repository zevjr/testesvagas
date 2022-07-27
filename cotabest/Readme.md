# Technical Test Cotabest

### Run test.
##### to run this test it is necessary to have previously installed and configured docker, for more information about it click [here](https://docs.docker.com/engine/install/)


- make the clone of this repository and enter the `cotabest` folder
- inside the folder execute this command
```
docker build . -t cotabest && docker run -p 5000:5000 cotabest
```
- access `http://localhost:5000/api/docs/` to see documentation
