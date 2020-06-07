import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.form['filename']
    print("Received file: {name}")
    with open('arnold_uploaded.jpg','wb') as f:
        file = next(req.files.items())
        b = file[1].read()
        f.write(b)
    return func.HttpResponse('Uploaded file \"{name}\"')