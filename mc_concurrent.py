import time
import memcache
# test
# Create a memcached client
client = memcache.Client(['localhost:11211'])

# Set a key with an initial value
key = 'my_key'
initial_value = 'Initial Value'
client.set(key, initial_value)

# Function to update the value of the key with a large value
def update_value():
    time.sleep(5)  # Simulating a time-consuming update
    new_value = 'Updated Value'
    client.set(key, new_value)
    print(f'Key "{key}" updated with value: {new_value}')

# Perform the update operation in a separate thread
import threading
thread = threading.Thread(target=update_value)
thread.start()

# Wait for a moment to allow the update operation to start
time.sleep(1)

# Perform a get request for the same key
retrieved_value = client.get(key)
print(f'Value retrieved from key "{key}": {retrieved_value}')

# Wait for the update operation to complete
thread.join()

# Retrieve the value after the update operation completes
retrieved_value_after_update = client.get(key)
print(f'Value retrieved after update from key "{key}": {retrieved_value_after_update}')
