import io
#import boto3
from request import put

from tornado.web import RequestHandler


s3 = boto3.client('s3')


class FileManagerService(RequestHandler):

    def post(self):
        """
        ---
        tags:
        - Core Forecast Service
        summary: uploads a file to S3 bucket  sinigerqa-backend-preprod 
        description: test 
        produces:
        - application/json
        parameters:
        -   name: upfile
            in: formData
            description: file to upload to s3
            required: true
            type: file
        responses:
            200:
              description: Comunicación establecida correctamente.
            500:
              description: No se pudo comunicar con el servidor.
            400:
              description: Bad Requests
        """
        try:
            file_object = io.BytesIO(self.request.files['upfile'][0]['body'])
            file_name = f'mgr-online/tmp/{self.request.files["upfile"][0]["filename"].replace(" ", "_")}'
            s3.upload_fileobj(
                file_object, 'preprod-backend-sinigerqa', file_name
            )
            mensaje = f'subida exitosa. probar en https://preprod-backend-sinigerqa.s3.amazonaws.com/mgr-online/tmp/{file_name}'
            err = False
        except Exception as e:
            err = True
            mensaje = e.__str__()

        self.write(
            dict(
                Estado=200,
                Error=err,
                Mensaje=mensaje
            )
        )



