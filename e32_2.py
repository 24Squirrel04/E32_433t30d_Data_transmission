import serial
import time

reset_set_config = bytes.fromhex('c4c4c4')
read_config = bytes.fromhex('c1c1c1')
aa = bytes.fromhex('c000061a1447')
bb = bytes.fromhex('00081816')
cc = '13'


def set_connection(el):
    ser.write(el)
    time.sleep(0.09)
    answer = ser.read_until().hex(':').split(':')
    time.sleep(0.5)
    print(answer)
    ser.close()
        
def write(read_coun):
        ser.write(read_coun)
        time.sleep(0.09)
        summ = ser.read_until().hex(':').split(':')
        print(summ)
        #ser.close()

def send(sen):
    while True:
        ser.write(sen)
        time.sleep(0.09)
        summ = ser.read_until().hex(':').split(':')
        print(summ)
        time.sleep(1)
    

def main():
    #write(aa)
    #set_connection(read_config)
    send(bb)
    
    
if __name__ == "__main__":
    try:
        ser = serial.Serial('COM4')            
        ser.baudrate = 9600
        ser.timeout = 0.02          
            
    except BaseException as ex:
        print(ex)
        print(f'No connect, trying to connect again!')
        time.sleep(5)
            
    else:
        main()
