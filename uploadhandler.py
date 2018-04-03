from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import utilities


class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        # Get the data (file) from the request
        upload = self.get_uploads()[0]
        # Get file name from the info of the file
        filename = blobstore.BlobInfo(upload.key()).filename

        utilities.add_file(upload, filename)

        self.redirect('/')
