#!/usr/bin/env python

import optparse
import os


CINDER_API_NODES = (
    "172.16.235.13",
    "172.16.235.18",
    "172.16.235.27")

CINDER_VOLUME_NODES = (
    "172.16.172.27",
    "172.16.172.48",
    "172.16.172.126")


def check_cinder_api_log(word):
    print "### Checking cidner-api log ###"
    for svr in CINDER_API_NODES:
        print "=== %s ===" % svr
        os.system("ssh %s grep %s /var/log/cinder/api.log" % (svr, word))
    print


def check_cinder_volume_log(word):
    print "### Checking cidner-volume log ###"
    for svr in CINDER_VOLUME_NODES:
        print "=== %s ===" % svr
        os.system("ssh %s grep %s /var/log/cinder/volume.log" % (svr, word))
    print


def check_cinder_backup_log(word):
    print "### Checking cidner-backup log ###"
    for svr in CINDER_VOLUME_NODES:
        print "=== %s ===" % svr
        os.system("ssh %s grep %s /var/log/cinder/backup.log" % (svr, word))
    print


def check_cinder_scheduler_log(word):
    print "### Checking cidner-scheduler log ###"
    for svr in CINDER_API_NODES:
        print "=== %s ===" % svr
        os.system("ssh %s grep %s /var/log/cinder/scheduler.log" % (svr, word))
    print

usage = 'usage: %prog [options] keyword'
parser = optparse.OptionParser(usage=usage)
parser.add_option("-a", "--api", action='store_true',
                  default=False, dest='api',
                  help="check cinder-api log")
parser.add_option("-v", "--volume", action='store_true',
                  default=False, dest='volume',
                  help="check cinder-volume log")
parser.add_option("-b", "--backup", action='store_true',
                  default=False, dest='backup',
                  help="check cinder-backup log")
parser.add_option("-s", "--scheduler", action='store_true',
                  default=False, dest='scheduler',
                  help="check cinder-scheduler log")

(options, remainder) = parser.parse_args()

if not remainder:
    print "No keyword provided. Run 'check_cinder_log.py -h' to show usage."
if options.api:
    check_cinder_api_log(remainder[0])
if options.volume:
    check_cinder_volume_log(remainder[0])
if options.backup:
    check_cinder_backup_log(remainder[0])
if options.scheduler:
    check_cinder_scheduler_log(remainder[0])
