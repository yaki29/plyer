'''
Sms
====

The :class:`Sms` provides access to sending Sms from your device.

Simple Examples
---------------

To send sms::

    >>> from plyer import sms
    >>> recipient = 9999222299
    >>> message = 'This is an example.'
    >>> sms.send(recipient=recipient, message=message)

'''


class Sms(object):
    '''Sms facade.

    .. note::

        On Android your app needs the SEND_SMS permission in order to
        send sms messages.

    .. versionadded:: 1.2.0

    '''

    def send(self, recipient, message):
        self._send(recipient=recipient, message=message)

    # private

    def _send(self, **kwargs):
        raise NotImplementedError()
