import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)  # max db = 15

redis_client.set("key", 'valor')


valor = redis_client.get('key')
valor = str(valor)
print(valor)


redis_client.set('key', 'value')

valor = redis_client.get('key')
valor = valor.decode('utf-8')
print(valor)

redis_client.delete('key')
