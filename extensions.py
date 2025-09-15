
ans=input("File name: ")
ans=ans.strip().lower()

if ".gif" in ans:
    print("image/gif")
elif ".jpg" in ans:
    print("image/jpeg")
elif ".jpeg" in ans:
    print("image/jpeg")
elif ".png" in ans:
    print("image/png")
elif ".pdf" in ans:
    print("application/pdf")
elif ".txt" in ans:
    print("text/plain")
elif ".zip" in ans:
    print("application/zip")
else:
    print("application/octet-stream")
