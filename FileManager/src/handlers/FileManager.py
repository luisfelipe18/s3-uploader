import io
import os
from abc import ABC

import boto3

from tornado.web import RequestHandler

s3 = boto3.client('s3')
bucket_name = 'preprod-backend-sinigerqa'


class FileManagerService(RequestHandler, ABC):

    def post(self):
        """
        ---
        tags:
        - Filemanager
        summary: uploads a file to S3 bucket sinigerqa-backend-preprod
        description: test 
        produces:
        - application/json
        parameters:
         -  name: upfile
            in: formData
            description: file to upload to s3
            required: true
            type: file
         -  name: modo
            in: formData
            description: W Saves file on disk, then upload with awscli with console. P reads file as bytes and uses boto3 client upload_fileobj  file. S Saves file on disk, then upload with boto3 client upload_file
            required: true
            type: string
        responses:
            200:
              description: Comunicación establecida correctamente.
            500:
              description: No se pudo comunicar con el servidor.
            400:
              description: Bad Requests
        """
        response_error, mensaje = None, None
        try:
            file_object = io.BytesIO(self.request.files['upfile'][0]['body'])
            file_name = f'mgr-online/tmp/{self.request.files["upfile"][0]["filename"].replace(" ", "_")}'
            modo = self.request.body_arguments['modo'][0].decode('utf8')

            if modo == 'P':
                s3.upload_fileobj(
                    file_object, bucket_name, file_name
                )
                mensaje = f'subida exitosa. probar en https://{bucket_name}.s3.amazonaws.com/mgr-online/tmp/{file_name}'
                response_error = False
            else:
                local_filename = self.request.files["upfile"][0]["filename"].replace(" ", "_")
                with open(local_filename, 'wb') as myfile:
                    myfile.write(self.request.files["upfile"][0]['body'])
                if modo == 'W':
                    os.system(
                        f'aws s3 cp {local_filename} s3://{bucket_name}/{file_name}'
                    )
                    mensaje = f'Success. probar en https://{bucket_name}.s3.amazonaws.com/mgr-online/tmp/{file_name}'
                    response_error = False
                elif modo == 'S':
                    s3.upload_file(
                        local_filename,
                        bucket_name,
                        file_name,
                    )

        except Exception as e:
            response_error = True
            mensaje = e.__str__()

        self.write(
            dict(
                Estado=200,
                Error=response_error,
                Mensaje=mensaje
            )
        )
