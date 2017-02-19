import boto3
import os


OUTPUT_DIR = '/s3site'

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
                print("uploading \"{}\"".format(full_key))
                bucket.put_object(Key=full_key, Body=auto)
