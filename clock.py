#!/usr/bin/python3

from StupidArtnet import StupidArtnet
import time,os,sys

# art net clock
# each digit has to be wired the same
# here comes the map to blame
# your time to be off
# just don't be in any shock!

# staring address: 0 is default

dmx_start_address = 0

refresh_time = 0.5 # sec

artnet = True

target_ip = '192.168.1.10'		# typically in 2.x or 10.x range
universe = 0 					# see docs

# each character is 7 bytes, and we have 6 characters, thats 42

packet_size = 42				# it is not necessary to send whole universe


# indexes are marked as follows, starting from 0:
# hour: 0 7  minutes: 14 21
# offset = digit * 7
#
# offset +
#   1
# 0   2
#   6
# 5   3
#   4

numbers = [
'1111110',
'0011000',
'0110111',
'0111101',
'1011001',
'1101101',
'1101111',
'0111000',
'1111111',
'1111101'
]



# CREATING A STUPID ARTNET OBJECT
# SETUP NEEDS A FEW ELEMENTS
# TARGET_IP   = DEFAULT 127.0.0.1
# UNIVERSE    = DEFAULT 0
# PACKET_SIZE = DEFAULT 512
# FRAME_RATE  = DEFAULT 30
a = StupidArtnet(target_ip, universe, packet_size)

print(a)

def send_sequence(sequence):
    i = dmx_start_address

    packet = bytearray()		# create packet for Artnet

    for char in sequence:
        if (char == '0'):
            packet.append(0x00)
        else:
            packet.append(0xFF)
        i+=1
    a.set(packet)
    a.show()

def main(argv):
    global numbers

    while True:
        time.sleep(refresh_time)
        # os.system("clear")

        h = time.localtime().tm_hour
        m = time.localtime().tm_min
        s = time.localtime().tm_sec
        time_str = f'{h:02}{m:02}{s:02}'

        sequence = ''
        for char in time_str:
            sequence = sequence + numbers[int(char)]

        # print(time_str + '\033[1;31m')
        print(sequence + '\033[1;31m')
        send_sequence(sequence)
        # print('\033[0m')

if __name__ == '__main__':
    main(sys.argv)