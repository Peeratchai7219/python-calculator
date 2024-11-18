class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0  # เริ่มต้นผลลัพธ์เป็น 0
        is_negative = False  # ตรวจสอบว่าผลลัพธ์ต้องเป็นลบหรือไม่
    
        # หาก b เป็นลบ ทำให้ b เป็นบวก และเปลี่ยนเครื่องหมายผลลัพธ์ตอนท้าย
        if b < 0:
            b = -b
            is_negative = True

        # วนลูป b ครั้งและบวก a เข้าไปใน result
        for _ in range(b):
            result = self.add(result, a)
            
        return -result if is_negative else result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")

        result = 0
        is_negative = (a < 0) ^ (b < 0)  # ตรวจสอบว่าผลลัพธ์ต้องติดลบหรือไม่ (XOR)

        # ใช้ค่าบวกเพื่อคำนวณ
        a, b = abs(a), abs(b)

        # ลบ b จาก a จนกว่าจะน้อยกว่า b
        while a >= b:
            a = self.subtract(a, b)
            result += 1

        return self.subtract(0, result) if is_negative else result

    
    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot perform modulo with divisor 0")

        # ตรวจสอบเครื่องหมายของ a และ b
        is_a_negative = a < 0
        is_b_negative = b < 0

        # ทำให้ a และ b เป็นค่าบวกด้วยการลบจาก 0
        if is_a_negative:
            a = self.subtract(0, a)
        if is_b_negative:
            b = self.subtract(0, b)

        # ลบ b จาก a จนกว่า a จะน้อยกว่า b
        while a >= b:
            a = self.subtract(a, b)   

        return self.subtract(0, a) if is_a_negative else a


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))