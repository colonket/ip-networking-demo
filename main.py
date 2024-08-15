def on_button_pressed_a():
    serial.write_line("")
    sendPacket(hardware_address2,
        "10.10.1.101",
        "10.10.1.102",
        "text",
        "Hello world! It's me! Margaret! Boy this message sure is long")
input.on_button_pressed(Button.A, on_button_pressed_a)

def sendPacketFragment(time_stamp: number, field: str, packet_fragment: str):
    global comm_buffer, field_count, iterator
    comm_buffer = ""
    field_count = 0
    iterator = 1
    for value in packet_fragment:
        comm_buffer = "" + comm_buffer + value
        if iterator % 14 == 0:
            radio.send_string("" + str(time_stamp) + field + str(field_count) + comm_buffer)
            comm_buffer = ""
            field_count += 1
        iterator += 1
    if comm_buffer != "":
        radio.send_string("" + str(time_stamp) + field + str(field_count) + comm_buffer)
def generateHexString(string_length: number):
    global hexadecimal_characters, hex_string, random_char
    hexadecimal_characters = "0123456789ABCDEF".split("")
    hex_string = ""
    for index in range(string_length):
        random_char = hexadecimal_characters._pick_random()
        hex_string = "" + hex_string + random_char
    return hex_string

def on_received_string(receivedString):
    serial.write_line(receivedString)
radio.on_received_string(on_received_string)

def sendPacket(hardware_address: str, source_ip: str, destination_ip: str, protocol: str, content: str):
    global msg_timestamp
    serial.write_line("[" + str(control.event_timestamp()) + "] " + hardware_address + " sent a packet!")
    msg_timestamp = input.running_time_micros() % 100
    sendPacketFragment(msg_timestamp, "M", hardware_address)
    sendPacketFragment(msg_timestamp, "S", source_ip)
    sendPacketFragment(msg_timestamp, "D", destination_ip)
    sendPacketFragment(msg_timestamp, "P", protocol)
    sendPacketFragment(msg_timestamp, "C", content)
def main():
    global hardware_address2
    radio.set_group(1)
    hardware_address2 = generateHexString(8)
    serial.write_line("Generated new MAC: " + hardware_address2)
msg_timestamp = 0
random_char = ""
hex_string = ""
hexadecimal_characters: List[str] = []
iterator = 0
field_count = 0
comm_buffer = ""
hardware_address2 = ""
split_packet: List[str] = []
main()

def on_forever():
    basic.show_string(hardware_address2)
basic.forever(on_forever)
