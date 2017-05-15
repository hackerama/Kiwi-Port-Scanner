#!/usr/bin/python3
#!Desenvolvedor: _carlosnericorreia_
#!email: hackerama@protonmail.com
# Kiwi Juicy Port Scanner v1.0


import queue
import threading
import socket
import time
print ("""

                                       
		  88      a8P  88                    88  
		  88    ,88'   ""                    ""  
		  88  ,88"                               
		  88,d88'      88 8b      db      d8 88  
		  8888"88,     88 `8b    d88b    d8' 88  
		  88P   Y8b    88  `8b  d8'`8b  d8'  88  
		  88     "88,  88   `8bd8'  `8bd8'   88  
		  88       Y8b 88     YP      YP     88   v1.0t

		    [+] Kiwi - Juicy Port Scanner [+]
			 por _carlosnericorreia_

""")
class ClasseThread(threading.Thread):
	def __init__(self, fila, tid):
		threading.Thread.__init__(self)
		self.fila = fila
		self.tid = tid
	
	def run(self):
		while True:
			porta = 0 
			try: 
				porta = self.fila.get(timeout=1)
			except queue.Empty:
				pass
				return			
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			res = s.connect_ex((ip, porta))
			if res == 0:
				print ("[+] Porta aberta encontrada: %d" % porta)
			s.close()
			self.fila.task_done()
			
				
ip = input("Digite o IP que deseja escanear: ")

fila = queue.Queue()
threadbank = []

for i in range(0,100):
	t = ClasseThread(fila, i)
	t.setDaemon(True)
	t.start()
	threadbank.append(t)

for porta in range (1,9999):
	fila.put(porta)

for item in threadbank:
	item.join()

print ("Scan Completo!")

