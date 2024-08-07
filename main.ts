function generateHexString(string_length: number): string {
    
    hexadecimal_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    hex_string = ""
    for (let index = 0; index < string_length; index++) {
        random_char = hexadecimal_characters._pickRandom()
        hex_string = hex_string + random_char
    }
    return hex_string
}

radio.onReceivedString(function on_received_string(receivedString: string) {
    
    split_packet = _py.py_string_split(receivedString, "~")
    serial.writeLine("" + hardware_address2 + " Received Size: " + ("" + split_packet.length))
    while (split_packet.length > 0) {
        serial.writeLine("" + hardware_address2 + " received " + split_packet.shift())
    }
    serial.writeLine("")
})
function sendPacket(hardware_address: string, source_ip: string, destination_ip: string, protocol: string, data: string) {
    
    packet = "" + hardware_address + "~" + source_ip + "~" + destination_ip + "~" + protocol + "~" + data
    radio.sendString(packet)
}

let packet = ""
let split_packet : string[] = []
let random_char = ""
let hex_string = ""
let hexadecimal_characters : string[] = []
let hardware_address2 = ""
radio.setGroup(1)
hardware_address2 = generateHexString(8)
serial.writeLine("Set MAC: " + hardware_address2)
serial.writeLine("")
sendPacket(hardware_address2, "10.10.1.101", "10.10.1.102", "text", "hello world")
basic.forever(function on_forever() {
    
})
