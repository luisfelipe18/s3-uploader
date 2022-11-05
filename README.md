# s3-uploader
uploads files to a s3 bucket

Usage:

install requirements: 
```
tornado_swagger==1.4.0
boto3
```

then run:

``` python main.py```

open browser and go to `localhost:8000/swagger`

Select `FileManager` and click on `Try It Out`
In parameter `Upfile`, select the word document from your disk.
In parameter `modo`, write `W`, `P` or `S` based on the desired behaivor for test:
 
 - `W` writed the object in `Upfile` into the disk, then python calls the terminal to upload the file with `awscli` using `aws s3 cp <localfile> <s3 uri destination>`
 - `P` read the object in `Upfile` from the requests and uses the `boto3` SDK for upload the object to bucket with `boto3.client('s3').upload_fileobj` to bucket.
 - 'S'  writed the object in `Upfile` into the disk and uses the `boto3` SDK for upload the file to bucket with `boto3.client('s3').upload_file` to bucket.


![image](https://user-images.githubusercontent.com/25039923/200093370-4fab947a-ed07-4788-839b-83051dcacc37.png)
