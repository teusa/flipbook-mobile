from boto3.dynamodb.conditions import Key

from tornado.web import authenticated

from webhandler import WebHandler


class FlipHandler(WebHandler):


    def get_images(self):
        s3client = self.boto_session.client('s3')
        for i in self.iterator['Items']:
            #if its an image at glacier it must be restored
            if 'Key' not in i:
                self.log.info("No Key???")
                continue
            url = s3client.generate_presigned_url(
                'get_object',
                Params={'Bucket': 'athena-security-imgs', 'Key': i['Key']},
                ExpiresIn=60 * 60 * 24 * 3,
                HttpMethod='GET')
            self.log.info("Yielding %s", url)
            yield url

    @authenticated
    def get(self, atm_name):
        table = self.dynamodb.Table('SecurityImagesTbl')
        #bucket = self.s3conn.Bucket('athena-security-imgs')
        self.iterator = table.query(KeyConditionExpression=Key('Machine').eq(atm_name),
                                    ScanIndexForward=False,
                                    Limit=80)

        self.render("security_img_viewer.html",
                    images=self.get_images)

