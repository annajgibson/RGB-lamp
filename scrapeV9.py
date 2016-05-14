#!/usr/bin/env python

# For Python 2.7.11
value = 0.1

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

from nltk.tokenize import TweetTokenizer
import pickle

import json
import os
import time

import sentiment_module as s

#import mraa library for controlling pins
import mraa

# define pin numbers (there will be three LEDs with each R,G,B wired to same pin)
redLedPin = 5
greenLedPin = 6
blueLedPin = 9

# define leds as pwm
redLed = mraa.Pwm(redLedPin)
greenLed = mraa.Pwm(greenLedPin)
blueLed = mraa.Pwm(blueLedPin)

# set led pins to output
redLed.enable(True)
greenLed.enable(True)
blueLed.enable(True)



##################
# AUTHENTICATION #
##################

# twitter_auth file contains authentication codes in json format.
with open('twitter_auth.json', 'r') as f:
     twitter_auth = json.load(f)

auth = OAuthHandler(twitter_auth["consumer_key"], twitter_auth["consumer_secret"])
auth.set_access_token(twitter_auth["access_token"], twitter_auth["access_secret"])

api = tweepy.API(auth)

#############
# STREAMING #
#############

class MyListener(StreamListener):

    def __init__(self, stat_in_use):
        super(MyListener, self).__init__()
        self.stat_in_use = stat_in_use
        #self.tokenizer = TweetTokenizer()

    def on_data(self, data):

        try:
            json_data = json.loads(data, "UTF-8")

            if "text" in json_data:
                tweet = json_data["text"]
                #tokenized = self.tokenizer.tokenize(tweet)
                sent = s.sentiment(tweet)
                print tweet.encode("utf-8"), sent.encode("utf-8")

                #check for tweet sentiment value
                value += 0.1
                if value > 1:
                    value = 0

            #if bad sentiment
                if value < 0.3:
                    redLed.write(0)
                    greenLed.write(1)
                    blueLed.write(1)
                #neutral sentiment
                elif value >= 0.3 and value < 0.6:
                    redLed.write(1)
                    greenLed.write(0)
                    blueLed.write(1)
                #good sentiment
                elif value >= 0.6 and value <= 1:
                    redLed.write(1)
                    greenLed.write(1)
                    blueLed.write(0)
                    #no sentiment read
                    #no sentiment read
                elif value < 0 or value > 1:
                #print ("bad value")
                    redLed.write(0)
                    greenLed.write(0)
                    blueLed.write(0)

        except BaseException as e:
            print "Error on_data: %s" % str(e)

        # Carry on streaming unless config.json file changed.
        return self.keep_streaming()

    def on_error(self, status):
        print status
        return self.keep_streaming()

    def keep_alive(self):
        return self.keep_streaming()

    def keep_streaming(self):
        stat_current = os.stat("config.json")
        return stat_current.st_mtime == self.stat_in_use.st_mtime and stat_current.st_size == self.stat_in_use.st_size

while True:
        
    with open("config.json", "r") as f:
        config = f.read()
        stat_in_use = os.fstat(f.fileno())
        listener = MyListener(stat_in_use)
        twitter_stream = tweepy.Stream(auth, listener)
        twitter_stream.filter(track=[config])


# When populating config.json, we need to create a new file e.g. temp32874.json, populate it and the rename this to config.json
# This avoids reading and writing at the same time.
# Secret/random file name in case webserver is serving multiple people.