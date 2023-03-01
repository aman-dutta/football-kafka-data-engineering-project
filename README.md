# Football Data Kafka - Data Engineering Project

## Introduction 
In this project, I executed an End-To-End Data Pipeline of football related keywords using Kafka.

## Architecture 
<img src="Architecture.jpg">

## Technology Used
- Python
- Snscrape
- Apache Kafka
- S3 Bucket
- Amazon Web Service(AWS)
- Glue Crawler
- EC2
- Athena

## Commands Used:

```
bin/zookeeper-server-start.sh config/zookeeper.properties  ----> Starting Zookeeper
Do a "sudo nano config/server.properties" - change ADVERTISED_LISTENERS to public ip of the EC2 instance  -----> For connecting with the EC2 instance
bin/kafka-topics.sh --create --topic footballTopic --bootstrap-server {Public IP of your EC2 Instance:9092} --replication-factor 1 --partitions 1
bin/kafka-console-producer.sh --topic footballTopic --bootstrap-server {Public IP of your EC2 Instance:9092} -----> Producer
bin/kafka-console-consumer.sh --topic footballTopic --bootstrap-server {Public IP of your EC2 Instance:9092}  -----> Consumer
```

### Footnote
Special mention to [Darshil Parmar](https://www.youtube.com/results?search_query=darshil+parmar) <br>
Please reach out to me in case of any queries. I would be happy to help! :smiley:
