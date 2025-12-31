import pika , json

def get_rabbitmq_channel():
    """Create a fresh RabbitMQ connection and channel."""
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host="rabbitmq",
            heartbeat=600,
            blocked_connection_timeout=300
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue='video', durable=True)
    return connection, channel

def upload(f, fs, channel, access):
    # store file in gridfs
    try:
        fid = fs.put(f)
    except Exception as err:
        print("error storing file: " + str(err))
        return "error storing file: " + str(err), 500
    
    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access['username']
    }
    
    # Create fresh connection for each publish to avoid stale channel issues
    connection = None
    try:
        connection, fresh_channel = get_rabbitmq_channel()
        fresh_channel.basic_publish(
            exchange='',
            routing_key='video',
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
    except Exception as err:
        fs.delete(fid)
        return "error queuing file for processing: " + str(err), 500
    finally:
        if connection and connection.is_open:
            connection.close()
