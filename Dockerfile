FROM python:3
ADD test.py /
RUN pip install pymongo
RUN pip install tweepy
RUN pip install dnspython
CMD [ "python", "./docker.py" ]