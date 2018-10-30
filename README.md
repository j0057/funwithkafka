# Fun with Kafka

## What's included

This is what the docker-compose cluster contains:

- *zookeeper*: a Zookeeper node
- *broker*: the actual Kafka broker; connects to zookeeper; can be scaled to multiple nodes
- *rest_proxy*
- *control_center*: exposes an HTTP control center UI on port _38000_
- *topics_ui*: exposes an HTTP UI for browsing topics on port _38001_

## Run it

Fire up a Kafka cluster:

    docker-compose up -d --scale broker=3

## Test it

There's a Python script. It needs the `confluent_kafka` library to run.

To install `pip` ("`p`ip `i`installs `p`ackages") --

    python3 <(curl https://bootstrap.pypa.io/get-pip.py) --user

To install `confluent_kafka`:

    python3 -m pip install --user confluent_kafka

Find out the IP of the first Kafka broker:

    docker exec kafka_broker_1 ip -4 a

Publish some messages to the `foo` topic:

    ./funwithkafka.py --address 172.24.0.5 --publish
