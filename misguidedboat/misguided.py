import time
import socket
 
def CheckValidIP(ip_adress):
    try:
        socket.inet_pton(socket.AF_INET, ip_adress)
        return True
    except socket.error:
        return False
 
def CheckPort(sent_ip, port_number, socket_item):
    try:
        socket_item.connect((
            sent_ip,
            port_number
        ))
        socket_item.close()
        return True
    except:
        return False
 
def VerboseCheckForPorts(sent_ip, socket_item, ending_index):
    for port_number in range(0, ending_index):
        checked_port = CheckPort(sent_ip, ending_index, socket_item)
 
        if checked_port:
            print(f"Port open on : {port_number}")
        else:
            print("... / closed port")
 
 
def FileCheckForPorts(sent_ip, socket_item, ending_index):
    found_ports = []
    failed_ports = []
 
    for port_number in range(1, ending_index):
        what_happened = CheckPort(sent_ip, port_number, socket_item)
 
        if what_happened:
            found_ports.append(port_number)
        else:
            failed_ports.append(port_number)
 
    return found_ports, failed_ports
 
def main():
    socket_connection = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )
 
    target_ip = input("Type IP to scan:\n")
    returned = CheckValidIP(target_ip)
 
    if returned:
        ending_port = int(input("\nWhat port do you wish to end your scan at? "))
        verbose_or_file = str(input("\nDo you wish for a verbose view or a file view?\nv / f\n"))
 
        start_time = time.time()
 
        if verbose_or_file == "f":
            print("Beginning file scan view...")
 
            success_ports, failed_ports = FileCheckForPorts(target_ip, socket_connection, ending_port)
 
            end_time = time.time() - start_time
 
            with open("Current_Port_Scan.txt", "w") as current_file:
                write = current_file.write
 
                write(f"Began scan at: {start_time}\nEnded scan at: {end_time}")
 
                for index in success_ports:
                    write(f"Found port: {index}")
                write("\n\n\n")
                for otherindex in failed_ports:
                    write(f"Failed to find port: {otherindex}")
        else:
            print("\nBeginning verbose scan...")
 
            VerboseCheckForPorts(target_ip, socket_connection, ending_port)
 
            end_time = time.time() - start_time
 
            print(f"Scan took: {end_time}")

main()
