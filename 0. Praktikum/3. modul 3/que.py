def queue():
  q=[]
  return q
def enqueue(q,data):
  q.insert(0,data)
  return q
def dequeue(q):
  data=q.pop()
  return data
def isEmpty(q):
  return (q==[])
def size(q):
  return (len(q))
