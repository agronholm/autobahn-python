###############################################################################
#
# The MIT License (MIT)
#
# Copyright (c) Tavendo GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
###############################################################################

from __future__ import absolute_import

from autobahn.wamp import websocket
from autobahn.twisted.websocket.protocol import WebSocketServerProtocol, \
    WebSocketServerFactory, WebSocketClientProtocol, WebSocketClientFactory

__all__ = (
    'WampWebSocketServerProtocol',
    'WampWebSocketServerFactory',
    'WampWebSocketClientProtocol',
    'WampWebSocketClientFactory',
)


class WampWebSocketServerProtocol(websocket.WampWebSocketServerProtocol, WebSocketServerProtocol):
    """
    Base class for Twisted-based WAMP-over-WebSocket server protocols.
    """


class WampWebSocketServerFactory(websocket.WampWebSocketServerFactory, WebSocketServerFactory):
    """
    Base class for Twisted-based WAMP-over-WebSocket server factories.
    """

    protocol = WampWebSocketServerProtocol

    def __init__(self, factory, *args, **kwargs):

        serializers = kwargs.pop('serializers', None)
        debug_wamp = kwargs.pop('debug_wamp', False)

        websocket.WampWebSocketServerFactory.__init__(self, factory, serializers, debug_wamp=debug_wamp)

        kwargs['protocols'] = self._protocols

        # noinspection PyCallByClass
        WebSocketServerFactory.__init__(self, *args, **kwargs)


class WampWebSocketClientProtocol(websocket.WampWebSocketClientProtocol, WebSocketClientProtocol):
    """
    Base class for Twisted-based WAMP-over-WebSocket client protocols.
    """


class WampWebSocketClientFactory(websocket.WampWebSocketClientFactory, WebSocketClientFactory):
    """
    Base class for Twisted-based WAMP-over-WebSocket client factories.
    """

    protocol = WampWebSocketClientProtocol

    def __init__(self, factory, *args, **kwargs):

        serializers = kwargs.pop('serializers', None)
        debug_wamp = kwargs.pop('debug_wamp', False)

        websocket.WampWebSocketClientFactory.__init__(self, factory, serializers, debug_wamp=debug_wamp)

        kwargs['protocols'] = self._protocols

        WebSocketClientFactory.__init__(self, *args, **kwargs)
