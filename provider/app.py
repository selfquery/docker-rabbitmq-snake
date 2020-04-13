from rabbit import emit
import time

while True:
    emit({'msg':'hello world'})
    time.sleep(1)