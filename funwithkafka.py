#!/usr/bin/env python3

import argparse
import logging
import sys

log = logging.getLogger(__name__)

def py_produce(address, topic):
    import kafka
    log.info('connecting to cluster')
    producer = kafka.KafkaProducer(bootstrap_servers=address, batch_size=0, linger_ms=0)
    try:
        for x in range(100):
            log.info('publishing value %d', x)
            producer.send(topic.encode('utf8'), key=b'foo', value=str(x).encode('utf8'))
    finally:
        log.info('closing producer')
        producer.close()

def py_consume(address, topic):
    import kafka

def cf_produce(address, topic):
    import confluent_kafka as cfkafka

def cf_consume(address, topic):
    import confluent_kafka as cfkafka

def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--produce', action='store_true', default=False)
    parser.add_argument('-c', '--consume', action='store_true', default=False)
    parser.add_argument('-a', '--address', default='172.20.0.3:9092')
    parser.add_argument('-L', '--library', choices=['py', 'cf'], default='cf')
    parser.add_argument('-t', '--topic', default='foo')
    return (parser, parser.parse_args(argv))

if __name__ == '__main__':
    parser, args = parse_args(sys.argv[1:])
    print(args)

    logging.basicConfig(level='DEBUG')

    produce = {'py': py_produce, 'cf': cf_produce}[args.library]
    consume = {'py': py_consume, 'cf': cf_consume}[args.library]

    if args.produce:
        produce(args.address, args.topic)
    elif args.consume:
        consume(args.address, args.topic)
    else:
        parser.print_help()
        sys.exit(1)
