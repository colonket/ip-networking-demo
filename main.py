def generateHexString(string_length: number):
    global hexadecimal_characters, hex_string, random_char
    hexadecimal_characters = "0123456789ABCDEF".split("")
    hex_string = ""
    for index in range(string_length):
        random_char = hexadecimal_characters._pick_random()
        hex_string = "" + hex_string + random_char
    return hex_string

def on_received_string(receivedString):
    global rebuilt_packet, split_packet
    rebuilt_packet = ""
    split_packet = receivedString.split("~")
    serial.write_line("" + hardware_address2 + " Received Size: " + ("" + str(len(split_packet))))
    while len(split_packet) > 0:
        serial.write_line("" + hardware_address2 + " received " + split_packet.shift())
    serial.write_line("")
radio.on_received_string(on_received_string)

def sendPacket(hardware_address: str, source_ip: str, destination_ip: str, protocol: str, data: str):
    global packet, packet_pieces, msg_timestamp
    serial.write_line("" + str((control.event_timestamp())))
    packet = "" + hardware_address + "~" + source_ip + "~" + destination_ip + "~" + protocol + "~" + data
    packet_pieces = [hardware_address, source_ip, destination_ip, protocol, data]
    msg_timestamp = input.running_time_micros() % 100
    for value in packet_pieces:
        radio.send_string("" + str(msg_timestamp) + "/" + value)
def main():
    global hardware_address2
    radio.set_group(1)
    hardware_address2 = generateHexString(8)
    serial.write_line("MAC: " + hardware_address2)
    sendPacket(hardware_address2,
        "10.10.1.101",
        "10.10.1.102",
        "text",
        "can you hear me? it's me margaret")
    serial.write_line(convert_to_text(input.running_time_micros()).substr(0, 4))
msg_timestamp = 0
packet_pieces: List[str] = []
packet = ""
hardware_address2 = ""
rebuilt_packet = ""
random_char = ""
hex_string = ""
hexadecimal_characters: List[str] = []
split_packet: List[str] = []
main()