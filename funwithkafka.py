#!/usr/bin/env python3

import argparse
import logging
import sys

import kafka

log = logging.getLogger(__name__)

def produce():
    log.info('connecting to cluster')
    producer = kafka.KafkaProducer(
        bootstrap_servers='172.20.0.2:9092',
        batch_size=0,
        linger_ms=0)
    try:
        for x in range(100):
            log.info('publishing value %d', x)
            producer.send(b'foo', key=b'foo', value=str(x).encode('utf8'))
    finally:
        log.info('closing producer')
        producer.close()

def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--produce', action='store_true', default=False)
    parser.add_argument('-c', '--consume', action='store_true', default=False)
    return (parser, parser.parse_args(argv))

if __name__ == '__main__':
    parser, args = parse_args(sys.argv[1:])
    print(args)

    logging.basicConfig(level='DEBUG')

    if args.produce:
        produce()
    elif args.consume:
        consume()
    else:
        parser.print_help()
        sys.exit(1)
