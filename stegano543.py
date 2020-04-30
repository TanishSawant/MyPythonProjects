from stegano import lsb
import wiki
inImg = 'paper.png'

outImg = 'topSecret.png'

message = wiki.get_full_info("Python")
lsb.hide(inImg, message=message).save(outImg)

msg = lsb.reveal(outImg)
print(f"Revealed message : {msg}")