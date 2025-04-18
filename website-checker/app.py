print("🔍 Website URL Checker")
url = input("Enter the URL to check: ")

if url.startswith("http://") or url.startswith("https://"):
    print("✅ Valid URL! This website uses HTTP/HTTPS.")
else:
    print("❌ Invalid URL! Please enter a valid HTTP/HTTPS URL.")
