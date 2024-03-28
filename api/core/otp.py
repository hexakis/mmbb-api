import pyotp
import pyqrcode

class OTP:
    @staticmethod
    def verify_otp(secret, otp):
        totp = pyotp.TOTP(secret)
        return totp.verify(otp)
    
    @staticmethod
    def generate_qr(data):
        qr_code = pyqrcode.create(data)
        return qr_code.png_as_base64_str()