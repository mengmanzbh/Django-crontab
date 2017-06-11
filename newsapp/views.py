from django.shortcuts import render
import time
# Create your views here.
def my_scheduled_job():
  print("OKOKOKOKOKOKOKOKOKOKOKO")
  fo = open("test.txt", "w")
  timestr = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
  fo.write(timestr)
  fo.close()
