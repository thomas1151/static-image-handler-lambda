import boto3
import os

s3 = boto3.client('s3')

client = boto3.client(
    's3',
    aws_access_key_id="ASIAX4J3VKAXVVZJ4N5V",
    aws_secret_access_key="Zov49FJBXGnmJg8RxcN6C+6N2JLIhcLJRWJ0nQYI",
    aws_session_token="FwoGZXIvYXdzEB8aDKHiWqUxnj+ZTAFvXiKCATSD8+tCXnF+z+1xcX19iMu8uKGnb78gzVWJUKUmRnDwnFcAbSZ0f4qaeMZDz7lPQu9KBKCMorHjaz5fsywGBnMxV1Gv1/zCAn5g1WJ8SFhh95bQwrPKM48ZSGNIbrUYMmIZAnrS3tOAEjs+YQ6NJNXHXYtMkDBWPkfXMwKgWjlaXfwo7o+ZiQYyKFCl7obp4fC/ik+JH0I6p+fQpSPjcNGfpEAB8gHRe02Bsv1ay1EETDU="
)

print('Request Image resized by S3 Object Lambda:')
image = client.get_object(
  Bucket='arn:aws:s3-object-lambda:eu-west-1:541827878959:accesspoint/test-cdn-tbarratt-image-lambda',
  Key='assets/post/2020-year-in-review/cover_200x200.jpg')["Body"]
if not os.path.exists("out"):
  os.mkdir('out')
with open('out/blob2.jpg','wb') as f:
  for i in image._raw_stream:
    f.write(i)
    f.close
print('Downloaded with Success')
