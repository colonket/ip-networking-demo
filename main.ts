input.onButtonPressed(Button.A, function () {
    serial.writeLine("")
    serial.writeLine("")
    serial.writeLine("")
    sendPacket(hardware_address, "10.10.1.101", "10.10.1.102", "text", "Hello world! It's me! Margaret! Boy this message sure is long")
})
function sendPacketFragment (time_stamp: number, field: string, packet_fragment: string) {
    comm_buffer = ""
    field_count = 0
    iterator = 1
    for (let value of packet_fragment) {
        comm_buffer = "" + comm_buffer + value
        if (iterator % 14 == 0) {
            radio.sendString("" + time_stamp + field + field_count + comm_buffer)
            comm_buffer = ""
            field_count += 1
        }
        iterator += 1
    }
    if (comm_buffer != "") {
        radio.sendString("" + time_stamp + field + field_count + comm_buffer)
    }
}
function generateHexString (string_length: number) {
    hexadecimal_characters = "0123456789ABCDEF".split("")
    hex_string = ""
    for (let index = 0; index < string_length; index++) {
        random_char = hexadecimal_characters._pickRandom()
        hex_string = "" + hex_string + random_char
    }
    return hex_string
}
radio.onReceivedString(function (receivedString) {
    serial.writeLine(receivedString)
})
function sendPacket (hardware_address: string, source_ip: string, destination_ip: string, protocol: string, content: string) {
    serial.writeLine("[" + control.eventTimestamp() + "]" + hardware_address + "sent a packet!")
    msg_timestamp = input.runningTimeMicros() % 100
    sendPacketFragment(msg_timestamp, "M", hardware_address)
    sendPacketFragment(msg_timestamp, "S", source_ip)
    sendPacketFragment(msg_timestamp, "D", destination_ip)
    sendPacketFragment(msg_timestamp, "P", protocol)
    sendPacketFragment(msg_timestamp, "C", content)
}
function main () {
    radio.setGroup(1)
    hardware_address = generateHexString(8)
    serial.writeLine("Generated new MAC: " + hardware_address)
}
let msg_timestamp = 0
let random_char = ""
let hex_string = ""
let hexadecimal_characters: string[] = []
let iterator = 0
let field_count = 0
let comm_buffer = ""
let hardware_address = ""
let split_packet: string[] = []
main()
basic.forever(function () {
    basic.showString(hardware_address)
})
