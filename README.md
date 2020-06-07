# serverless-fileupload

An Azure Functions example written in Python to upload files using a multipart form.

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

func host start

curl -v -F filename=arnold.jpg -F upload=@arnold.jpg http://localhost:7071/api/upload
```