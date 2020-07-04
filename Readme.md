#SCHC implemetation for LoRaWAN packet creation

This document contains details and information on the different modules used to implement the SCHC protocol (mainly Header compression and, if necessary, DLMS payload fragmentation) to transmit DLMS data over a LoRaWAN network on the Uplink side. The details of the working of each module, the dataflow and the variables used in each module to achieve the same have been highlighted here. All the modules have been designed and implemented keeping in mind the IPv6 protocol and its features.

[Google](https://www.google.co.in)
##Table of contents:
1. [Introduction](#introduction)
2. [Hello Darling](#hello-darling)

##Introduction :
The LoRaWAN packet that is to be transmitted has a limited bandwidth of 125KHz for reasons such as power constraints on the devices and the on-going spectral fued. Because of these reasons, at any given point in time the maximum amount of data that can be transmitted is 51 bytes. These 51 bytes of data must include everything including the header of the LoRaWAN packet, the header of the actual DLMS payload(IPv6 header) and the DLMS payload itself. Due to said constraints, the transmission would be very efficient if one could compress the data with a set of fixed(static) rules (constraints) given on both the transmitter and the receiver sides. Thus the SCHC(Static Context Header Compression) protocol is used to compress the header and if necessary fragment the DLMS payload data. The fragmentation is carried out if the payload data is bigger than what can be accommodated in the LoRaWAN packet and each successive part of the fragments are sent in successive LoRaWAN packets. It is to be noted that in any and all parts of this particular document, since it only discusses the Uplink, the terms ‘Transmitter’ and ‘Receiver’ refer to the Radio Gateway (RGW) and the Network Gateway (NGW) respectively unless otherwise mentioned.

For furthur information on the SCHC protocol this [link](https://datatracker.ietf.org/doc/rfc8724/?include_text=1) can be visited.



##

