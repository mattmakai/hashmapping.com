import boto3
import os


OUTPUT_DIR = '/s3site'

def upload_with_content_type(file, full_key, auto):
    if ".html" in file:
        print("uploading \"{}\" as html".format(full_key))
        bucket.put_object(Key=full_key, Body=auto, ACL='public-read',
                          ContentType="text/html")
    elif ".css" in file:
        print("uploading \"{}\" as css".format(full_key))
        bucket.put_object(Key=full_key, Body=auto, ACL='public-read',
                          ContentType="text/css")
    else:
        print("uploading \"{}\"".format(full_key))
        bucket.put_object(Key=full_key, Body=auto,
                          ACL='public-read')


if __name__ == "__main__":
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('www.hashmapping.com')
    for root, dirs, files in os.walk(os.getcwd() + '/s3site'):
        subdir = root[(len(os.getcwd())+len(OUTPUT_DIR)):len(root)]
        if subdir.startswith('/'):
            subdir = subdir[1:]
        for file in files:
             with open(os.path.join(root, file), "r") as auto:
                full_key = file
                if subdir:
                    full_key = subdir + '/' + file
                upload_with_content_type(file, full_key, auto)


