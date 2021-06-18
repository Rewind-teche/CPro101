import dropbox

class UploadFiles:

    def __init__(self,access_token):

        self.access_token = access_token

    def uploadFiles(self,files_from,files_to):

        dbx = dropbox.Dropbox(self.access_token)

        fileHandler = open(files_from,"rb")
        dbx.files_upload(fileHandler.read(),files_to)


def main():
    access_token = "sl.Ay2qOKOP4GMcpQH9NpgwnbqM2O0PFhwcLaDqSHks3VrCzw2nrxO4K5dX1N04ioPVEFjEu8t4qg7CijA7lNihcVIpa9HOjRg9dMG_9bOUQ-y3p0jEPVyD1W0WffunqUEXleyezBbriUNw"
    uploadFiles = UploadFiles(access_token)

    files_from  = input("Enter the path of the file you want to upload into the dropbox : ")
    files_to = "/UploadFiles/img.jpg"

    uploadFiles.uploadFiles(files_from, files_to)
    print("File uploaded successfully")


main()