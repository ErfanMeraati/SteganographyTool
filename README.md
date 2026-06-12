# 🕵️ Steganography Tool

Hide secret messages inside PNG images  invisible to the naked eye.  
پیام مخفی داخل تصویر PNG — بدون هیچ تغییر قابل‌مشاهده‌ای.

---

## 🇬🇧 English

### What it does
Hides any text message inside a PNG image using the **LSB (Least Significa Bit)** technique.  
Each pixel stores 1 bit of your message. The image looks identical — but the secret is there.

### Usage

**Hide a message:**
```bash
python steganography_tool.py encode

**Extract a message:**
bash
python steganography_tool.py decode

**Or just run the EXE and follow the prompts.**

### ⚠️ Important
> Output file **must be PNG**. JPG uses lossy compression and will destroy the hidden data.

### Build EXE
bash
pyinstaller --onefile steganography_tool.py

### Requirements

pip install pillow

---

## 🇮🇷 فارسی

###یکار می‌کنه؟
هر پیام متنی رو داخل یه تصویر PNG مخفی می‌کنه با تکنیک **LSB**.  
تصویر ظاهراً هیچ فرقی نمی‌کنه — ولی پیام داخلشه.

### نحوه استفاده

**مخفی کردن پیام:**
bash
python steganography_tool.py encode

**استخراج پیام:**
bash
python steganography_tool.py decode

**یا فقط فایل EXE رو اجرا کن و مراحل رو دنبال کن.**

### ⚠️ نکته مهم
> فایل خروجی حتماً باید **PNG** باشه. JPG فشرده‌سازی lossy داره و پیام رو نابود می‌کنه.

### ساخت فایل اجرایی
bash
pyinstaller --onefile steganography_tool.py

### پیش‌نیاز

pip install pillow
