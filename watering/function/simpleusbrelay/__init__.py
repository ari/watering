#!/usr/bin/python
#author: Patrick Jahns (patrick.jahns@gmail.com)
# https://raw.githubusercontent.com/patrickjahns/simpleusbrelay/master/simpleusbrelay/__init__.py

import usb.core
import usb.util



class simpleusbrelay(object):
        #config for byte arrays
        #devices on
        byte_devices_on = [\
        [0xFE, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],\
        [0xFF, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],\
        [0xFF, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],\
        [0xFF, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],\
        [0xFF, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],\
        [0xFF, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],\
        [0xFF, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],\
        [0xFF, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],\
        [0xFF, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]\
        ]
        #devices off array
        byte_devices_off = [\
        [0xFC, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],\
        [0xFD, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],\
        [0xFD, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],\
        [0xFD, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],\
        [0xFD, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],\
        [0xFD, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],\
        [0xFD, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],\
        [0xFD, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],\
        [0xFD, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]\
        ]
        def __init__(self,Vendor,Product ):
                self.idVendor = Vendor
                self.idProduct = Product
                self.dev = usb.core.find(idVendor=Vendor, idProduct=Product)
                if self.dev is None:
                        raise ValueError('Device not found')

        def __send_msg(self, msg):
                interface=0
                reattach=False
                if self.dev.is_kernel_driver_active(interface) is True:
                                reattach=True
                                try:
                                        self.dev.detach_kernel_driver(interface)
                                except Exception as e:
                                        pass # already unregistered

                self.dev.set_configuration()
                sentmsg = "".join(chr(n) for n in msg)
                self.dev.ctrl_transfer(0x21,0x09,0x0300,0x0000,sentmsg,1000)
                if reattach:
                        try:
                                self.dev.detach_kernel_driver(interface)
                        except Exception as e:
                                pass # already unregistered

        def array_on(self, array_number):
                if (array_number < 0 or array_number > 8) and array_number is not 'all':
                        raise ValueError('Not proper array defined, must be 1-8 or all')
                else:
                        if array_number is not 'all':
                                self.__send_msg(self.byte_devices_on[array_number])
                        else:
                                self.__send_msg(self.byte_devices_on[0])

        def array_off(self, array_number):
                if (array_number < 0 or array_number > 8) and array_number is not 'all':
                        raise ValueError('Not proper array defined, must be 1-8 or all')
                else:
                        if array_number is not 'all':
                                self.__send_msg(self.byte_devices_off[array_number])
                        else:
                                self.__send_msg(self.byte_devices_off[0])

