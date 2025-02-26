import struct

EXIF_TAGS = {
    256: "ImageWidth",
    257: "ImageHeight",
    271: "Make",
    272: "Model",
    274: "Orientation",
    282: "XResolution",
    283: "YResolution",
    296: "ResolutionUnit",
    306: "DateTime",
    531: "YCbCrPositioning",
    34665: "ExifOffset",
    34853: "GPSInfo",
}

# Data type sizes (bytes per entry)
TYPE_SIZES = {
    1: 1,  # BYTE
    2: 1,  # ASCII (string)
    3: 2,  # SHORT (2 bytes)
    4: 4,  # LONG (4 bytes)
    5: 8,  # RATIONAL (8 bytes)
}

def read_exif(filename):
    with open(filename, "rb") as f:
        if f.read(2) != b'\xFF\xD8':  # JPEG Start of Image (SOI) marker
            return None

        while True:
            byte = f.read(2)
            if not byte:
                break

            if byte == b'\xFF\xE1':  # EXIF APP1 Marker
                length_bytes = f.read(2)
                exif_length = struct.unpack('>H', length_bytes)[0]
                exif_data = f.read(exif_length - 2)

                print(f"First 10 bytes of EXIF section: {exif_data[:10]}")

                # Skip "Exif\x00\x00" (6 bytes)
                if exif_data[:6] == b'Exif\x00\x00':
                    exif_data = exif_data[6:]

                # Check byte order
                byte_order = exif_data[0:2]
                if byte_order == b'II':
                    endian = '<'  # Little Endian
                elif byte_order == b'MM':
                    endian = '>'  # Big Endian
                else:
                    print(f"Unknown byte order: {byte_order}")
                    return None

                print(f"Byte Order: {byte_order.decode()} ({'Little' if endian == '<' else 'Big'} Endian)")

                # TIFF validation
                tiff_magic = struct.unpack(endian + 'H', exif_data[2:4])[0]
                if tiff_magic != 0x002A:
                    print("Invalid TIFF magic number")
                    return None

                # IFD Offset
                ifd_offset = struct.unpack(endian + 'I', exif_data[4:8])[0]
                num_entries = struct.unpack(endian + 'H', exif_data[ifd_offset:ifd_offset + 2])[0]
                ifd_offset += 2

                print(f"Number of EXIF entries: {num_entries}")

                # Parse IFD Entries
                for _ in range(num_entries):
                    tag_entry = exif_data[ifd_offset:ifd_offset + 12]
                    tag_id, tag_type, tag_count, tag_value_offset = struct.unpack(endian + 'HHII', tag_entry)

                    tag_name = EXIF_TAGS.get(tag_id, f"Unknown ({tag_id})")
                    data_size = TYPE_SIZES.get(tag_type, 1) * tag_count

                    if data_size <= 4:
                        # Data stored directly in tag_value_offset field
                        value = tag_value_offset
                    else:
                        data_offset = tag_value_offset
                        value = exif_data[data_offset:data_offset + data_size]
                    
                        if tag_type == 2:  # ASCII String
                            value = value.decode(errors="ignore").strip("\x00")
                        
                        elif tag_type == 5:  # RATIONAL (Numerator/Denominator)
                            numerator, denominator = struct.unpack(endian + 'II', value)
                            if denominator != 0:
                                value = numerator / denominator
                            else:
                                value = "Invalid (Zero Denominator)"
                    print(f"{tag_name}: {value}")

                    # Move to next IFD entry
                    ifd_offset += 12
                print(num_entries)
                return exif_data
    return None


filename = "./examples/cat.gif"
filename = "./examples/ErasTour.jpg"
filename = "./examples/Taylor_TTPD.jpeg"

exif_data = read_exif(filename)

if exif_data:
    print("EXIF Data Found!")
else:
    print("No EXIF data found.")
