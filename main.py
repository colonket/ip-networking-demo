def generateHexString(string_length: number):
    global hexadecimal_characters, hex_string, random_char
    hexadecimal_characters = ["0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f"]
    hex_string = ""
    for index in range(string_length):
        random_char = hexadecimal_characters._pick_random()
        hex_string = "" + hex_string + random_char
    return hex_string

def on_received_string(receivedString):
    global split_packet
    split_packet = receivedString.split("~")
    serial.write_line("" + hardware_address2 + " Received Size: " + ("" + str(len(split_packet))))
    while len(split_packet) > 0:
        serial.write_line("" + hardware_address2 + " received " + split_packet.shift())
    serial.write_line("")
radio.on_received_string(on_received_string)

def sendPacket(hardware_address: str, source_ip: str, destination_ip: str, protocol: str, data: str):
    global packet
    packet = "" + hardware_address + "~" + source_ip + "~" + destination_ip + "~" + protocol + "~" + data
    radio.send_string(packet)
packet = ""
random_char = ""
hex_string = ""
hexadecimal_characters: List[str] = []
hardware_address2 = ""
split_packet: List[str] = []
radio.set_group(1)
hardware_address2 = generateHexString(8)
serial.write_line("Set MAC: " + hardware_address2)
serial.write_line("")
sendPacket(hardware_address2,
    "10.10.1.101",
    "10.10.1.102",
    "text",
    "hello world")

def on_forever():
    pass
basic.forever(on_forever)
