let msg_timestamp = 0
let packet_pieces: string[] = []
let packet = ""
let rebuilt_packet = ""
let random_char = ""
let hex_string = ""
let hexadecimal_characters: string[] = []
let hardware_address2 = ""
let split_packet: string[] = []




function main () {
    radio.setGroup(1)
    hardware_address2 = generateHexString(8)
    serial.writeLine("MAC: " + hardware_address2)
    sendPacket(
        hardware_address2,
        "10.10.1.101",
        "10.10.1.102",
        "text",
        "can you hear me? it's me margaret"
    )
    serial.writeLine(convertToText(input.runningTimeMicros()).substr(0, 4))
}

function generateHexString (string_length: number) {
    hexadecimal_characters = "0123456789ABCDEF".split()
    hex_string = ""
    for (let index = 0; index < string_length; index++) {
        random_char = hexadecimal_characters._pickRandom()
        hex_string = "" + hex_string + random_char
    }
    return hex_string
}
radio.onReceivedString(function (receivedString) {
    rebuilt_packet = ""
    split_packet = _py.py_string_split(receivedString, "~")
    serial.writeLine("" + hardware_address2 + " Received Size: " + ("" + split_packet.length))
    while (split_packet.length > 0) {
        serial.writeLine("" + hardware_address2 + " received " + split_packet.shift())
    }
    serial.writeLine("")
})
function sendPacket (hardware_address: string, source_ip: string, destination_ip: string, protocol: string, data: string) {
    serial.writeLine("" + (control.eventTimestamp()))
    packet = "" + hardware_address + "~" + source_ip + "~" + destination_ip + "~" + protocol + "~" + data
    packet_pieces = [
    hardware_address,
    source_ip,
    destination_ip,
    protocol,
    data
    ]
    msg_timestamp = input.runningTimeMicros() % 100
    for (let value of packet_pieces) {
        radio.sendString("" + msg_timestamp + "/" + value)
    }
}

main()