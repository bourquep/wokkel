from twisted.python import log
from twisted.internet import task
from subprotocols import XMPPHandler

# From https://mailman.ik.nu/pipermail/twisted-jabber/2008-October/000171.html
class KeepAlive(XMPPHandler):

    interval = 300
    lc = None
    logPings = False

    def connectionInitialized(self):
        self.lc = task.LoopingCall(self.ping)
        self.lc.start(self.interval)

    def connectionLost(self, *args):
        if self.lc:
            self.lc.stop()

    def ping(self):
        if self.logPings:
            log.msg("Stayin' alive")
        self.send(" ")
