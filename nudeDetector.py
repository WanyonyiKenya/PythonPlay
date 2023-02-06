from nudenet import NudeClassifier 


#in images
f = NudeClassifier()
newData=f.classify('../newpy.jpg')
print(newData)

#in videos
newVid = f.clssify("sample vid")
print(newVid)

#you get the proportions of nudity n the files using nudenet