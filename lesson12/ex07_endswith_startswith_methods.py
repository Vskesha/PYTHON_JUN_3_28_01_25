# str.endswith(suffix[, start[, end]])
# suffix: один рядок або кортеж рядків

filename = "example.png"
print(filename.endswith(".png"))  # True
print(filename.startswith("file"))  # False

url = "https://example.com/index.html"
print(url.endswith((".html", ".htm")))  # True
print(url.startswith(("ttps://", "http"), 1))  # True
