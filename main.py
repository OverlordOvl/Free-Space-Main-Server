import os
import pickle
from abc import ABC

from twisted.protocols.basic import NetstringReceiver

from twisted.internet import protocol, reactor

from twisted.python import failure
from dotenv import load_dotenv

from API import contoller


load_dotenv()


class MainProtocol(NetstringReceiver, ABC):
    def connectionMade(self):
        # self.sendString("pong")

        pass

    def sendString(self, string: str or bytes):
        if type(string) == str:
            string = string.encode('utf-8')
        super(MainProtocol, self).sendString(string)

    def stringReceived(self, data):
        data = pickle.loads(data)
        self.sendString(pickle.dumps(contoller.compare_new_server(data)))


class MainServer(protocol.Factory):
    protocol = MainProtocol


reactor.listenTCP(8000, MainServer())
reactor.run()
