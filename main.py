import os 


#vmrun_path = '"C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmrun.exe"'
vmrun_path = "vmrun.exe"

def get_running_vm():
    
    cmd = vmrun_path + " " + "list" + " >>output.txt"
    os.system(cmd)

    
    with open("output.txt", "r") as file1:
        Lines = file1.readlines()

        count = 0
        running_vm_path = []
        print("List to running VM")
        for line in Lines:
            count += 1
            if(count>1):
                running_vm_path.append(line.strip())
                print(line.strip())
    
    cmd = "del output.txt"
    os.system(cmd)
    return running_vm_path

def stop_running_vm(vmx_path):
    count = 0
    for x in vmx_path:
        cmd = vmrun_path + " " + "-T ws stop " + '"' + str(vmx_path[count]) + '"'
        os.system(cmd)
        print(str(vmx_path[count]) + " was Stopped")
        count += 1


running_vm_path = get_running_vm()

stop_running_vm(running_vm_path)

