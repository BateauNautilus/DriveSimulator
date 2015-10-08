# Message Format

## Arbitration ID

How to convert ids ?

* device_id = ((30A & 0xF00)>>16) = 3
* message_id = (30A & 0x0FF) = 10

## Data
This is an example to how to calculate a message and what it means for easy
interpretation.

### Motor Status

data :
> vcan0  30A   [8]  07 D0 45 80 3C 00 00 00

means:

| Name          | data      | value     |
|---------------|-----------|-----------|
| device_id     | 3         | 3         |
| message_id    | 0A        | 10        |
| rpm           | 0x07,0xD0 | 2000      |
| voltage       | 0x45,0x80 | 5.5V      |
| current       | 0x3c,0x00 | 1A        |
| vibration     | 0x00,0x00 | vibration |

### Environment Status

data :
>   vcan0  30B   [4]  45 00 2F AE


| Name              | data      | value     |
|-------------------|-----------|-----------|
| device_id         | 3         | 3         |
| message_id        | 0B        | 11        |
| waterTemperature  | 0x45,0x00 | 5 celcius |
| humidity          | 0x2F,0xAE | 0.12      |
