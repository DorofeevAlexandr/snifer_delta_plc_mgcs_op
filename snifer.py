import keyboard
import serial


class Snifer:    
    def __init__(self,
                 port='COM1',
                 baudrate=9600, 
                 bytesize=7,
                 parity='N',
                 stopbits=1,
                 timeout=1):
        
        self.ser = serial.Serial(port=port, 
                                baudrate=baudrate, 
                                bytesize=bytesize,
                                parity=parity,
                                stopbits=stopbits,
                                timeout=timeout)
        print(self.ser)
        self.requests = set()

    # ser.write(b'command')
    def read_port(self):
        self.data = self.ser.readline()
        if not(self.data in self.requests):
            self.requests.add(self.data)
            result = [self.data[i:i+1] for i in range(0, len(self.data))]
            print(self.data)
            print(result)
            return result

    def port_close(self):
        self.ser.close()


if __name__ == '__main__':
    panel_op = Snifer()
    
    print('')
    print('Для остановки нажмите кнопку "escape"')
    while True:
            new_request = panel_op.read_port()
            if keyboard.is_pressed("escape"):
                print("Выход")
                break
