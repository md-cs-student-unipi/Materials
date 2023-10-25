import os

# List all the file names
file_names = [
    "Intro and style.md",
    "Internet Of Things.md",
    "Interoperability and Standards.md", 
    "MQTT.md",
    "Many Faces of IoT.md",
    "ZigBee standard.md",
    "High Tech Greenhouse and DOREMI.md",
    "IoT Design Aspects.md",
    "Exercises on Approaches of Duty Cycle.md",
    "Biologging.md",
    "MAC Protocols.md",
    "802.15.4.md",
    "Embedded Systems and Case study of Arduino.md",
    "Energy Harvesting IoT.md",
    "Hands-on on Thingspeak.md",
    "Arduino and TinyML Hands-on.md", 
    "Indoor Localization.md",
    "Wireless Sensor Network.md", 
    "The ZigBee Network Layer.md",
    #Paganelli (wireless and mobile) part
    "Wireless networks.md", 
    "Mobile Network.md", 
    "IEEE 802.11.md",
    "Software Defined Networking.md",
    "Network Function Virtualization.md",
    "ComNetsEmu - Hands On.md",
    "Hands-on Network slicing.md",
    "An Introduction to the Theory of Signals.md",
    "Fourier Transform.md", "Fast Fourier Transform.md",
    "Analog to digital conversion.md"
    ]
# Create a new file to hold the concatenated text
output_file = open("MPCS.md", "w")

i = 1
# Loop through the file names and add their contents to the output file
for file_name in file_names:
    with open('pages/'+file_name, "r") as file:
        # Add a page break before the header of each chapter
        if i != 1:
            output_file.write("\n <div style='page-break-after: always'></div> \n\n\n")
            # Add the filename as a header to the output file
            output_file.write(f"# Chapter {i-1}: {file_name[:-3]}\n")
        # Add the contents of the file to the output file
        output_file.write(file.read())
        # Add a newline character between files
        output_file.write("\n")
        i += 1

# Close the output file
output_file.close()

print("Files concatenated into MPCS.md")
