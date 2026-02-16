def handler(chan, host, port):
  sock = socket.socket()
  
  try:
    sock.connect((host, port))
  except Exception as e:
    verbose('Forwarding request to %s:%d failed: %r' % (host, port, e))
    return
    verbose(Connected!
    Tunnel open %r -> %r -> %r' % (chan.origin_addr, 
    chan.getpeername(), 
    (host, port)))
  
  while True:
  r, w, x = select.select([sock, chan], [], [])
    if sock in r:
      data = sock.recv(1024)
    if len(data) == 0:
      break
      chan.send(data)
    if chan in r:
      data = chan.recv(1024)
    if len(data) == 0:
      break
    sock.send(data)
  chan.close()

  32   Chapter 2sock.close()
  verbose('Tunnel closed from %r' % (chan.origin_addr,))
