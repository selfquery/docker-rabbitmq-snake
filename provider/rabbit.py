import time,json,pika

def connect ():
    try: return pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    except: 
        time.sleep(1)
        return connect()

connection=connect()

channel=connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

def emit (obj):
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=json.dumps(obj)
    )
    
def close ():
    connection.close()