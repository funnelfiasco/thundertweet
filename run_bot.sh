#!/bin/bash

(/home/bcotton/devel/thundertweet/thundertweet.py && /home/bcotton/SpiderOak/bin/oysttyer -hold=5 -status='https://www.youtube.com/watch?v=v2AC41dglnM #INwx #ThunderBot (Thunder reported at KLAF in last 10 minutes)') >> /home/bcotton/log/thundertweet-$(date +%Y%m%d)
