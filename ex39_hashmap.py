def new(num_buckets = 256):
    """Initializes a Map with the given number of buckets."""
    aMap = []
    for i in range(0, num_buckets):
	    aMap.append([])
    # aMap is a list of 256 empty lists (buckets)
    return aMap
	
def hash_key(aMap, key):
    """Given a key this will create a number and then convert it to an index for the aMap's buckets."""
    # return the index (as a interger from 0 to 255) for the given key
    return hash(key) % len(aMap)
	
def get_bucket(aMap, key):
    """Given a key, find the bucket where it would go."""
    bucket_id = hash_key(aMap, key)
    # return the bucket (as a list) for the given key
    return aMap[bucket_id]
	
def get_slot(aMap, key, default = None):
    """
    Returns the index, key, and value of a slot found in a bucket.
    Returns -1, key, and default (None if not set) when not found.
    """
    # this variable bucket is just a pointer which points to the actual bucket in aMap.
    bucket = get_bucket(aMap, key)
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            # the existing (index, key, value)
    	    return i, k, v
    # key does not exist
    return -1, key, default
	
def get(aMap, key, default=None):
    """Gets the value in a bucket for the given key, or the default."""
    i, k, v = get_slot(aMap, key, default=default)
    return v
	
def set(aMap, key, value):
    """Sets the key to the value, replacing any existing value."""
    bucket = get_bucket(aMap, key)
    i, k, v = get_slot(aMap, key)
    
    if i >= 0:
	    # the key exists, replace it
	    bucket[i] = (key, value)
    else:
	    # the key does not, append to create it
	    bucket.append((key, value))
		
def delete(aMap, key):
    """Deletes the given key from the Map."""
    bucket = get_bucket(aMap, key)
	
    for i in xrange(len(bucket)):
	    k, v = bucket[i]
	    if key == k:
		    del bucket[i]
		    break
			
def list(aMap):
    """Prints out what's in the Map."""
    for bucket in aMap:
	    if bucket:
		    for k, v in bucket:
			    print k, v
	