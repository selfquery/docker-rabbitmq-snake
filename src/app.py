from rabbit import channel
import time

while True:
    method,props,message=channel.basic_get('task_queue')
    if method: print(message)