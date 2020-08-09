FROM python:3
ADD docker.py /
RUN pip install pymongo
RUN pip install tweepy
RUN pip install dnspython
CMD [ "python", "./docker.py" ]