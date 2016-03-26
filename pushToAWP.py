import boto3
import sys

if len(sys.argv) == 1:
	print "PUT A FILE AS ARGUMENT"
	sys.exit(0)
else:
	fileName = sys.argv[1]

print 'Argument List:', str(sys.argv)

s3 = boto3.resource('s3')

print "First iteration"
for bucket in s3.buckets.all():
	print bucket.name

print 
print "Uploading File"
toUpload = open(fileName, 'rb')
s3.Bucket('clockwork.bucket').put_object(Key=fileName, Body=toUpload)


print
print "File should be added"
