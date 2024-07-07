import qrcode
def generate_qr(data,version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=40,border=4,fill_color="black",back_color="white",output_filename="qroutput.png"):
    qr=qrcode.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=box_size,
        border=border
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill_color=fill_color,back_color=back_color)
    img.save(output_filename)

