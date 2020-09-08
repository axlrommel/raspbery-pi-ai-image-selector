# image-classifier

get docker image from https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html


run it locally with access to folder

`docker run -p 8888:8888 -v "$PWD":/home/jovyan jupyter/tensorflow-notebook`


copy model.json and group1-shard1of1.bin to s3 bucket. make those two files public