
t = [
  {"id": 80231, "coco_url": "http://images.cocodataset.org/train2017/000000080231.jpg", "flickr_url": "http://farm3.staticflickr.com/2572/3742388669_433bc69b76_z.jpg"},
  {"id": 86208, "coco_url": "http://images.cocodataset.org/train2017/000000086208.jpg", "flickr_url": "http://farm4.staticflickr.com/3287/2419467924_dcabe79e79_z.jpg"},
  {"id": 307337, "coco_url": "http://images.cocodataset.org/train2017/000000307337.jpg", "flickr_url": "http://farm6.staticflickr.com/5018/5402054922_0c9804abed_z.jpg"},
  {"id": 500603, "coco_url": "http://images.cocodataset.org/train2017/000000500603.jpg", "flickr_url": "http://farm7.staticflickr.com/6220/6287044300_f2e4e97489_z.jpg"},
  {"id":255317,"coco_url":"http://images.cocodataset.org/train2017/000000255317.jpg","flickr_url":"http://farm3.staticflickr.com/2558/3696750357_ee1ec758cd_z.jpg"}]
image_urls = [coco_url for id, coco_url in t[0]]
print(image_urls)
# for img in image_urls:
#     # We can split the file based upon / and extract the last split within the python list below:
#     file_name = img.split('/')[-1]
#     print(f"This is the file name: {file_name}")
#     # Now let's send a request to the image URL:
#     r = requests.get(img, stream=True)
#     # We can check that the status code is 200 before doing anything else:
#     if r.status_code == 200:
#         # This command below will allow us to write the data to a file as binary:
#         with open(file_name, 'wb') as f:
#             for chunk in r:
#                 f.write(chunk)
#     else:
#         # We will write all of the images back to the broken_images list:
#         broken_images.append(img)