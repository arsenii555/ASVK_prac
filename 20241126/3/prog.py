import struct
import sys


def parse_wav_header():
    data = sys.stdin.buffer.read(44)

    if len(data) < 44:
        print("NO")
        return

    riff, size, wave, fmt, fmt_length, audio_format, channels, rate, byte_rate, block_align, bits_per_sample, data_marker, data_size = struct.unpack(
        '<4sI4s4sIHHIIHH4sI', data)

    if riff != b'RIFF' or wave != b'WAVE' or fmt != b'fmt ' or data_marker != b'data':
        print("NO")
        return

    header_info = (
        f"Size={size + 8}, "
        f"Type={audio_format}, "
        f"Channels={channels}, "
        f"Rate={rate}, "
        f"Bits={bits_per_sample}, "
        f"Data size={data_size}"
    )
    print(header_info)


parse_wav_header()
