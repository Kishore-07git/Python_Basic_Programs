# Input:Number of bits
bits=int(input("Enter the number of bits:"))

bytes_=bits/8
kilobytes=bytes_/1024
megabytes=kilobytes/1024
gigabytes=megabytes/1024
terabytes=gigabytes/1024
# output
print(f"{bits} bits is equivalent to:")
print(f"Bytes {bytes_}")
print(f"KiloBytes {kilobytes}")
print(f"MegaBytes {megabytes}")
print(f"GigaBytes {gigabytes}")
print(f"TeraBytes {terabytes}")